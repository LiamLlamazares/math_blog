-- Mana kit shortcodes for Quarto.  Declare in a post's front matter:
--   shortcodes: [../_kit/mana.lua]
--   {{< mana UR >}}   {{< card lightning-bolt >}}   {{< cards a b c >}}   {{< duel lucky >}}
-- HTML output uses classes prefixed mk-.  Other formats get plain text.

-- ---------------------------------------------------------------- helpers
local function script_dir()
  local src = debug.getinfo(1, "S").source
  if src:sub(1, 1) == "@" then src = src:sub(2) end
  return src:match("^(.*)[/\\][^/\\]*$") or "."
end
local DIR = script_dir()

local function read_file(rel)
  local f = io.open(DIR .. "/" .. rel, "rb")
  if not f then error("mana.lua: cannot read " .. DIR .. "/" .. rel) end
  local s = f:read("a")
  f:close()
  return s
end

local function esc(s)
  return (tostring(s):gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"):gsub('"', "&quot;"))
end

local function strip_tags(s)
  return (s:gsub("<[^>]*>", ""))
end

local function is_html()
  return quarto.doc.is_format("html")
end

local function arg_string(args)
  local parts = {}
  for _, a in ipairs(args) do parts[#parts + 1] = pandoc.utils.stringify(a) end
  return table.concat(parts, " ")
end

local function words(args)
  local out = {}
  for _, a in ipairs(args) do
    for w in pandoc.utils.stringify(a):gmatch("[^%s,]+") do out[#out + 1] = w end
  end
  return out
end

local function raw(ctx, html)
  if ctx == "block" then return pandoc.RawBlock("html", html) end
  return pandoc.RawInline("html", html)
end

local function plain(ctx, text)
  if ctx == "block" then return pandoc.Para({ pandoc.Str(text) }) end
  return pandoc.Str(text)
end

-- ---------------------------------------------------------------- data
local cards_by_id, card_order
local function cards()
  if not cards_by_id then
    local data = quarto.json.decode(read_file("cards.json"))
    cards_by_id, card_order = {}, {}
    for _, c in ipairs(data.cards) do
      cards_by_id[c.id] = c
      card_order[#card_order + 1] = c.id
    end
  end
  return cards_by_id
end

local function get_card(id)
  local c = cards()[id]
  if not c then
    error("mana.lua: unknown card '" .. tostring(id) .. "'. Known: " .. table.concat(card_order, ", "))
  end
  return c
end

-- ---------------------------------------------------------------- once-per-document includes
local SYMBOLS = { "W", "U", "B", "R", "G", "C", "T", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" }
local NAMES = {
  W = "white", U = "blue", B = "black", R = "red", G = "green", C = "colourless", T = "tap",
}
local function symbol_name(k)
  if NAMES[k] then
    if k == "T" then return "tap symbol" end
    return NAMES[k] .. " mana"
  end
  return k .. " generic mana"
end

local included = {}
local function once(key, fn)
  if included[key] then return end
  included[key] = true
  fn()
end

local function ensure_sprite()
  once("sprite", function()
    local defs = {}
    for _, k in ipairs(SYMBOLS) do
      local s = read_file("symbols/" .. k .. ".svg")
      local inner = s:gsub("^%s*<svg[^>]*>", ""):gsub("</svg>%s*$", "")
      inner = inner:gsub("id='([^']*)'", function(i) return "id='mk-" .. k .. "-" .. i .. "'" end)
      inner = inner:gsub("url%(#([^)]*)%)", function(i) return "url(#mk-" .. k .. "-" .. i .. ")" end)
      inner = inner:gsub("href='#([^']*)'", function(i) return "href='#mk-" .. k .. "-" .. i .. "'" end)
      defs[#defs + 1] = "<symbol id='mk-sym-" .. k .. "' viewBox='0 0 100 100'>" .. inner .. "</symbol>"
    end
    quarto.doc.include_text("after-body",
      "<svg width='0' height='0' style='position:absolute' aria-hidden='true' focusable='false'><defs>"
      .. table.concat(defs) .. "</defs></svg>")
  end)
end

local function ensure_fonts()
  once("fonts", function()
    quarto.doc.include_text("in-header",
      '<link rel="preconnect" href="https://fonts.googleapis.com">'
      .. '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      .. '<link href="https://fonts.googleapis.com/css2?family=Alegreya+SC:wght@700&family=Cinzel:wght@700&family=EB+Garamond:ital,wght@0,500;0,700;1,500&display=swap" rel="stylesheet">')
  end)
end

local function ensure_duel_js()
  once("duel.js", function()
    quarto.doc.include_text("after-body", "<script>" .. read_file("duel.js") .. "</script>")
  end)
end

-- ---------------------------------------------------------------- symbols
local function pip(k)
  ensure_sprite()
  return "<svg class='mk-pip' viewBox='0 0 100 100' role='img' aria-label='" .. symbol_name(k)
      .. "'><use href='#mk-sym-" .. k .. "'/></svg>"
end

local function valid_symbol(k)
  for _, s in ipairs(SYMBOLS) do if s == k then return true end end
  return false
end

local function cost_html(cost)
  local out = {}
  for k in cost:gmatch(".") do
    if valid_symbol(k) then out[#out + 1] = pip(k) end
  end
  return table.concat(out)
end

-- text with {X} tokens -> html with pips
local function rich(t)
  return (esc(t):gsub("{(.)}", function(k)
    if valid_symbol(k) then return pip(k) end
    return "{" .. k .. "}"
  end))
end

-- ---------------------------------------------------------------- cards
local function name_style(c)
  local avail = 12.9
  local s = math.min(1.3, (avail - 1.4 * #c.cost) / (#c.name * 0.52))
  -- #c.name counts bytes; good enough (a curly apostrophe counts three, which only shrinks it slightly)
  return string.format(" style='font-size:%.2fem'", s)
end

local function cost_label(c)
  if c.cost == "" then return "land" end
  local names = {}
  for k in c.cost:gmatch(".") do names[#names + 1] = symbol_name(k) end
  return "cost " .. table.concat(names, ", ")
end

local function card_html(c, small)
  ensure_fonts()
  local pt = ""
  if c.pt then
    local s, r = c.pt:match("^(%d+)/(%d+)$")
    pt = "<div class='mk-pt'><div><span class='mk-pl'>Strength</span> <b>" .. s .. "</b></div>"
        .. "<div><span class='mk-pl'>Resilience</span> <b>" .. r .. "</b></div></div>"
  end
  -- lands that make one or two colours: large symbol(s) in the text box, a small badge on the art
  local big, gives = "", ""
  if c.big and c.big ~= "" then
    local ps = {}
    for k in c.big:gmatch(".") do ps[#ps + 1] = pip(k) end
    big = "<div class='mk-makes'>Makes</div><div class='mk-big'>" .. table.concat(ps, "<span class='mk-or'>or</span>") .. "</div>"
    local gs = {}
    for k in c.big:gmatch(".") do gs[#gs + 1] = pip(k) end
    gives = "<span class='mk-gives' aria-hidden='true'><i>+</i>" .. table.concat(gs) .. "</span>"
  end
  local classes = "mk-card mk-f-" .. c.frame .. (#c.frame == 2 and " mk-split" or "") .. (small and " mk-sm" or "")
  return "<div class='" .. classes .. "' role='group' aria-label='" .. esc(c.name) .. ", " .. cost_label(c)
      .. "'><div class='mk-in'>"
      .. "<div class='mk-nb'><span class='mk-nm'" .. name_style(c) .. ">" .. esc(c.name) .. "</span>"
      .. "<span class='mk-cost'>" .. cost_html(c.cost) .. "</span></div>"
      .. "<div class='mk-art mk-img-" .. c.id .. "' role='img' aria-label='Artwork for " .. esc(c.name) .. "'>" .. gives .. "</div>"
      .. "<div class='mk-tb'><span>" .. esc(c.type) .. "</span></div>"
      .. "<div class='mk-tx" .. (c.pt and " mk-ctr" or "") .. (big ~= "" and " mk-land" or "") .. ((big ~= "" and not c.text:find("^Makes")) and " mk-land2" or "") .. "'>" .. big .. ((big ~= "" and c.text:find("^Makes")) and "" or ("<p>" .. rich(c.text) .. "</p>")) .. "</div>"
      .. pt .. "</div></div>"
end

local function band(ident)
  local pal = { W = "#f1e4a6", U = "#9ccbf1", B = "#b8b1c6", R = "#f1a290", G = "#a4d49d" }
  local cs = {}
  for k in ident:gmatch(".") do cs[#cs + 1] = pal[k] end
  if #cs == 1 then return cs[1] end
  return "linear-gradient(90deg," .. table.concat(cs, ",") .. ")"
end

-- Each artist is credited the first time their card appears in a post, and not again.
local credited = {}
local function credit_html(list)
  local parts = {}
  for _, c in ipairs(list) do
    if not credited[c.id] then
      credited[c.id] = true
      parts[#parts + 1] = esc(c.name) .. ": " .. esc(c.artist)
    end
  end
  if #parts == 0 then return "" end
  return "<p class='mk-credit'>Art. " .. table.concat(parts, "; ") .. ".</p>"
end

-- ---------------------------------------------------------------- shortcodes
local M = {}

-- {{< mana UR >}}  {{< mana 1UU >}}  {{< mana "2 W" >}}
M["mana"] = function(args, kwargs, meta, raw_args, ctx)
  local s = arg_string(args):gsub("[%s{}]", "")
  local syms = {}
  for k in s:gmatch(".") do
    k = k:upper()
    if not valid_symbol(k) then
      error("mana.lua: unknown mana symbol '" .. k .. "' in {{< mana " .. s .. " >}}")
    end
    syms[#syms + 1] = k
  end
  if not is_html() then
    local t = {}
    for _, k in ipairs(syms) do t[#t + 1] = "{" .. k .. "}" end
    return plain(ctx, table.concat(t))
  end
  local out = {}
  for _, k in ipairs(syms) do out[#out + 1] = pip(k) end
  return raw("inline", "<span class='mk-mana'>" .. table.concat(out) .. "</span>")
end

-- {{< card lightning-bolt >}}
M["card"] = function(args, kwargs, meta, raw_args, ctx)
  local ids = words(args)
  local c = get_card(ids[1])
  if not is_html() then return plain(ctx, c.name) end
  return raw(ctx, "<div class='mk-single'>" .. card_html(c, false) .. credit_html({ c }) .. "</div>")
end

-- {{< cards a b c >}}
M["cards"] = function(args, kwargs, meta, raw_args, ctx)
  local list = {}
  for _, id in ipairs(words(args)) do list[#list + 1] = get_card(id) end
  if not is_html() then
    local n = {}
    for _, c in ipairs(list) do n[#n + 1] = c.name end
    return plain(ctx, table.concat(n, ", "))
  end
  local out = {}
  for _, c in ipairs(list) do out[#out + 1] = card_html(c, false) end
  return raw(ctx, "<div class='mk-cards'><div class='mk-row'>" .. table.concat(out) .. "</div>"
    .. credit_html(list) .. "</div>")
end

-- {{< duel lucky >}}   one game, by id, from duel.json
M["duel"] = function(args, kwargs, meta, raw_args, ctx)
  local data = quarto.json.decode(read_file("duel.json"))
  local gid = words(args)[1]
  local g
  for _, x in ipairs(data.games) do if x.id == gid then g = x end end
  if not g then
    local ids = {}
    for _, x in ipairs(data.games) do ids[#ids + 1] = x.id end
    error("mana.lua: duel needs a game id, one of: " .. table.concat(ids, ", "))
  end
  local used, list = {}, {}
  local function use(id)
    if not used[id] then used[id] = true; list[#list + 1] = get_card(id) end
  end
  for _, f in ipairs(g.frames) do
    for _, z in ipairs({ f.hand, f.lands, f.cast }) do
      for _, id in ipairs(z) do use(id) end
    end
  end
  if not is_html() then
    local items = {}
    for _, f in ipairs(g.frames) do
      items[#items + 1] = { pandoc.Plain({ pandoc.Str(f.title .. ". " .. (strip_tags(f.say):gsub("’", "'"))) }) }
    end
    return pandoc.BulletList(items)
  end
  ensure_duel_js()
  local tpls = {}
  for _, c in ipairs(list) do
    tpls[#tpls + 1] = "<template data-id='" .. c.id .. "' data-name='" .. esc(c.name) .. "'>"
        .. card_html(c, true) .. "</template>"
  end
  local text = quarto.json.encode({ games = { g } })
  assert(not text:find("</script", 1, true), "duel.json must not contain </script")
  return raw(ctx, "<div class='mk-duel' data-mk-duel role='group' aria-label='" .. esc(g.label) .. "'>"
    .. "<script type='application/json' class='mk-data'>" .. text .. "</script>"
    .. table.concat(tpls)
    .. "<div class='mk-play'></div><div class='mk-final'></div>"
    .. "<noscript><p>This figure steps through a practice game and needs JavaScript.</p></noscript>"
    .. credit_html(list) .. "</div>")
end

return M
