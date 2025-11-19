Future

Things to implement
1. Improve GUI of blog (brainstorm options for this)
2. Improve coment system to something that supports latex and is more proggesional (does not include emojis as the current one)
2. Make creating and editingposts easier by implementing the following
    a) All latex files for blogposts are in the Blog_latex folder. When one of these files is edited the relevant post should be updated.
    b) The post is updated as follows: Pandoc is run as detailed in the mathematica conversion file. Then The mathematica file is run on the output to convert this to markdown. The conversion step should be implemented in a python file instead with calls pandoc and then applies the same rules as in the mathematica file (or possibl a cleaner version on them to generate the outputted post).
    c) Once the conversion is done the relevant post in the _posts folder is updated
    d) One the girhub repository is pushed the blog updates online per normal

3. Implement a way of testing how a markdown file looks without creating a whole blog post