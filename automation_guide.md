# Automation Guide: Mailchimp RSS-to-Email

To eliminate the manual effort of sending emails for every new post, follow these steps to set up an automated RSS-to-Email campaign in Mailchimp.

## 1. Get Your Feed URL
Your blog's RSS feed is located at:
`https://nowheredifferentiable.com/index.xml`

*(Note: Ensure your latest site build is deployed so this file is accessible to Mailchimp).*

## 2. Create the Campaign in Mailchimp
1.  Log in to Mailchimp and go to **Automations** > **Pre-built Journeys** (or search for **RSS-to-Email**).
2.  Select **Share blog updates**.
3.  Enter your Feed URL: `https://nowheredifferentiable.com/index.xml`.
4.  Choose the **frequency** (e.g., "Every day at 10:00 AM" or "Every week"). Mailchimp will only send an email if there is a new post in the feed.

## 3. Apply the Template
1.  In the **Design** step of your campaign, choose **Code Your Own** or paste the content from [post_notification.html](file:///c:/Users/liaml/Documents/GitHub/Research/math_blog/post_notification.html) into a Text/HTML block.
2.  The template uses Mailchimp's merge tags (like `*|RSSITEM:CONTENT_FULL|*`) to automatically pull in your post's content and title.

## 4. Test and Activate
1.  Use the **Preview and Test** feature in Mailchimp to see how it looks with your latest post.
2.  **Activate** the automation.

Now, whenever you publish a new post using Quarto, Mailchimp will detect the change in `index.xml` and handle the delivery for you. No more hand-crafting emails!
