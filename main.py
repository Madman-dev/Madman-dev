name: Latest DevDojo blog post workflow
on:
  schedule:
    # Runs every day
    - cron: '0 0 * * *'
  workflow_dispatch:

jobs:
  update-readme-with-blog:
    name: Update this repo's README with latest blog posts
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: gautamkrishnar/blog-post-workflow@master
        with:
          comment_tag_name: "DEVDOJO"
          feed_list: "https://v2.velog.io/rss/jacks222"
          commit_message: "Update Madman-dev blog posts"
          gh_token: ${{ secrets.GITHUB_TOKEN }}
