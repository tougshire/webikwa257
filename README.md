# Webikwa257

Webikwa257 is a blog app for Wagtail

## Important Note

This project is in development and there may be breaking changes until this note is removed

## Installation

Webikwa257 requires webikwa_templates, touglates and wagtail_modeladmin. If you're using a different template app than webikwa_templates, you can substitute that app

These instructions are written with the assumption that you're starting a new project

- create a new Wagtail project (see [Wagtail's instructions](https://docs.wagtail.org/en/v6.2.1/getting_started/) )
  - This will work if you stop after creating the superuser, but the rest of the tutorial covers features that might be useful 
- pip install [wagtail-markdown](https://pypi.org/project/wagtail-markdown/)
- pip install [wagtail_modeladmin](https://pypi.org/project/wagtail-modeladmin/)
- pip install [recurring-ical-events](https://pypi.org/project/recurring-ical-events/)
- pip install [nh3](https://pypi.org/project/nh3/)
- git clone [https://github.com/tougshire/touglates](https://github.com/tougshire/touglates)
- git clone [https://github.com/tougshire/webikwa_templates](https://github.com/tougshire/webikwa_templates)
- git clone [https://github.com/tougshire/webikwa257](https://github.com/tougshire/webikwa257)
- add the following to INSTALLED_APPS in settings/base.py:
  - "wagtail.contrib.settings",
  - "wagtail_modeladmin",
  - "wagtailmarkdown",
  - "wagtail.contrib.table_block",
  - "touglates",
  - "webikwa_templates",
  - "webikwa257",
- Add the following to your settings:

```
WAGTAILMARKDOWN = {
    "autodownload_fontawesome": True,
    "extensions": ['extra'],
}
```

- run the migrations again
- run collectstatic

## Setting Up Tutorial

### Basic setup making use of a featured article page and a redirect page

- run the server and browse to the dashboard (http(s)://[your_url_or_ip]/admin/)
- rename the automatically-created page
  - in the dashboard, click "Pages", then the edit icon (a pencil) for the automatically created page (which may be "home" or "welcome ..." or something like that)
  - If the title of the page is "Home", change the title to "Home-Old".
    In the promote tab, rename the slug from "home" to "home-old".
  - publish the page
- create a new article index page
  - using the "add child page" action next to the word "Root", create a new article index page
  - title it "Articles"
  - publish the page
- create a new article static tags index page
  - from the root page, create a new article static tags index page
  - title it "Featured Articles"
  - under "Tags included" enter: \_featured1,\_featured2;\_featured3,\_featured4;\_featured5
  - publish the page
- create a new redirect page
  - from root, create a new redirect page
  - title it "Home"
  - for the target page, choose the featured articles page
  - publish the page
- move the featured articles page and the articles index page under the home page
  - from the page list under root, check the checkboxes next to Featured Articles and Articles
  - click the "move" button
  - click the three dots next to "Root" and "Choose another page"
  - choose Home
  - Click "Yes, move these pages"
- make Home the root page for the default site
  - click "Settings" then "Sites"
  - choose the default site (probably the only site, "localhost")
  - change the root page from the old home page to the new home page (which is the redirect page)
  - save the change

### Adding featured articles

- Add articles by clicking "Articles" in the sidebar. Tag each with one of "\_f1", "\_f2", "\_f3", or ""\_f4". Publish each article
  - Note that because \_f1 and \_f2 are both in the first tag group (you grouped tags with with semicolons in an earlier step), and because "show body instead of summary" was 1, the entire body is shown instead of the summary for articles with those tags

### Adding sidebar articles

- Create a single tag page
  - Click "Pages" from the side menu, then "Home"
  - Click the icon to add a page and and choose "Article Static Tags Index Page"
  - For "title" type "About"
  - For "tags included" type "about"
- Create a sidebar page
  - From the admin sidebar, click "Pages" then "Home"
  - Click the icon for a new page, then choose "Sidebar page"
  - For the title, type "Left Sidebar"
  - Uncheck "Show pagetitle"
  - For location, choose "Left"
  - Publish the page
- Enable the sidebar
  - In the admin sidebar, click "Settings", then "Site Template Settings"
  - Check "Show leftbar"
  - Save the settings
- Create a sidebar menu
  - Click "Sidebar Articles" then "Add Sidebar Article Page"
  - For "Page Title" type "Main Menu"
  - In "Body md" type the following:

```markdown
- [home](/)
- [about](/about)
```

- - publish the page
- Create an article with the "About" Tag
  - Click "Articles", then "Add an article"
  - For the title type "About me"
  - For tags, type "about"
  - Type anyth appropriate for summary and body
  - Publish the page
  - Visit the site and check the menu
- Create a Sidebar Calendar
  - Create an Icalendar Index Page
    - Click "Pages", then "Home"
    - Click the child page icon and click "Icalendar Index Page"
    - For title, enter "iCalendars"
    - Publish the page
  - Create an Icalendar Page
    - Click "icalendars", then "Add icalendar page" 
    - For page title, enter "Python Software Foundation Events"
    - For source, enter "https://www.google.com/calendar/ical/3haig2m9msslkpf2tn1h56nn9g@group.calendar.google.com/public/basic.ics"
    - Publish the page
  - Creae a Combiner Page and Add it to the sidebar
    - Click "Pages", then "Home", then the child page icon ">" for "Left Sidebar"
    - Click the icon to add a child page
    - Choose "Icalendar Combiner"
    - For title, enter "Python Events"
    - Select the Python Software Foundation Calendar
    - Publish the page
