# saulbaizman-teaching.github.io

This repository is the source code for a one-page static website that houses an index of all courses I have taught since 2014. (Note: some links point to closed systems such as Slack and Discord. Websites with "403 Forbidden" errors have likely been disabled via `.htaccess` on the web host.)


[Visit courses.baizman.com.](https://courses.baizman.com)

## manual updates

Add the appropriate course name and course to the corresponding CSV files. Then run the command below:

```sh
python3 make-website-toc.py > index.html
```

## automatic updates

Add the appropriate course name and course to the corresponding CSV files. The `regenerate-index.yml` workflow will automatically regenerate `index.html` and commit it back to the repository.
