# ArticleSpider
This directory contains the source for the `ArticleSpider`.

# Running the spider
Currently, the spider just trawls `drstevesavage.com` and collects
the URLs that it followed. It doesn't go outside of this domain because
we restrict it with `allowed_domains`.

You can run the spider with (in the root of the project) :

```
$ make spider
```

If you'd like to save the output to file, run:

```
make spider_to_json
```

Please check the `items.json` that it produces to see the resulting output.

# Overview
A summary of each file and it's purpose:

### spider.py
The spider itself. Currently accepts a single `allowed_domain` and `start_url`
from `settings.py` and returns a list of `PageItem`.

As @arsenal9971 moves forward with the actual parsing that will be performed in
`pipelines.py`, I will work on bringing the Django app (logic discussed before)
that passes the domains to `ArticleSpider`.

### settings.py
`scrapy` and custom settings to control behaviour of the spider.

### pipelines.py
After the spider retrieves some HTML from a URL, we pass it through
our `pipeline` as defined by `ITEM_PIPELINES` in `settings.py`. Currently,
there is nothing happening here except logging.

I expect all our parsing logic to be contained within `pipelines.py`.

### items.py
Our model file. This is the shape of the data we expect the spider to
generate when it scrapes the URLs. For now, we just take the URL,
so, `PageItem` only has one attribute, `url`.

# Testing
You can find associated tests in the `test/` folder in the project root.
