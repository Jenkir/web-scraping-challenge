{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dependencies\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as  pd\n",
    "import requests\n",
    "import time\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - ====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 89.0.4389\n",
      "[WDM] - Get LATEST driver version for 89.0.4389\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Driver [C:\\Users\\Jenkir\\.wdm\\drivers\\chromedriver\\win32\\89.0.4389.23\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "#Executable path to driver\n",
    "def init_browser():\n",
    "executable_path = {\"executable_path': chromedriver.exe\"}\n",
    "return Browser(\"chrome\", **executable_path, headless=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape ():\n",
    "    browser = init_browser()\n",
    "    mars_data = {}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#visit Mars news site via Splinter module\n",
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's Mars 2020 Rover Completes Its First Drive\n",
      "In a 10-plus-hour marathon, the rover steered, turned and drove in 3-foot (1-meter) increments over small ramps.\n"
     ]
    }
   ],
   "source": [
    "#create html object\n",
    "html = browser.html\n",
    "\n",
    "#parse HTML using Beautiful Soup\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "#scrape site and collect latest news title and paragraph text\n",
    "news_title = soup.find('div', class_='content_title').text\n",
    "news_par = soup.find('div', class_='article_teaser_body').text\n",
    "\n",
    "#display scraped data\n",
    "print(news_title)\n",
    "print(news_par)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# JPL Mars Space Images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#visit Mars featured space image site via Splinter\n",
    "featured_image_url = 'https://spaceimages-mars.com/image/featured/mars1.jpg'\n",
    "browser.visit(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.comhttps://spaceimages-mars.com/image/featured/mars1.jpg'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#create html object\n",
    "html_image = browser.html\n",
    "main_url = 'https://spaceimages-mars.com'\n",
    "#parse html using Beautiful Soup\n",
    "soup = BeautifulSoup(html_image, 'html.parser')\n",
    "\n",
    "featured_image_url = main_url + featured_image_url\n",
    "#display link to featured image\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Description</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [Description, Value]\n",
       "Index: []"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#visit Mars Facts webpage and scrape table containing facts about the planet\n",
    "mars_facts_url = 'https://galaxyfacts-mars.com'\n",
    "\n",
    "browser.visit(mars_facts_url)\n",
    "#time.sleep(1)\n",
    "mars_facts_html = browser.html\n",
    "mars_facts_soup = BeautifulSoup(mars_facts_html, 'html.parser')\n",
    "\n",
    "fact_table = mars_facts_soup.find('table', class_='table table-striped')\n",
    "column1 = fact_table.find_all('td', class_='column-1')\n",
    "column2 = fact_table.find_all('td', class_='column-2')\n",
    "\n",
    "facets = []\n",
    "values = []\n",
    "\n",
    "for row in column1:\n",
    "    facet = row.text.strip()\n",
    "    facets.append(facet)\n",
    "    \n",
    "for row in column2:\n",
    "    value = row.text.strip()\n",
    "    values.append(value)\n",
    "    \n",
    "mars_facts = pd.DataFrame({\n",
    "    \"Description\":facets,\n",
    "    \"Value\":values\n",
    "    })\n",
    "\n",
    "mars_facts_html = mars_facts.to_html(header=False, index=False)\n",
    "mars_facts\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Jenkir\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py:501: FutureWarning: browser.find_link_by_text is deprecated. Use browser.links.find_by_text instead.\n",
      "  FutureWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Cerberus Hemisphere Enhanced\n",
      "\n",
      "https://marshemispheres.com/images/full.jpg\n",
      "\n",
      "Schiaparelli Hemisphere Enhanced\n",
      "\n",
      "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg\n",
      "\n",
      "Syrtis Major Hemisphere Enhanced\n",
      "\n",
      "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg\n",
      "\n",
      "Valles Marineris Hemisphere Enhanced\n",
      "\n",
      "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg\n"
     ]
    }
   ],
   "source": [
    "# scrape images of Mars' hemispheres from astrogeology site\n",
    "mars_hemisphere_url = 'https://marshemispheres.com'\n",
    "hemi_dicts = []\n",
    "\n",
    "for i in range(1,9,2):\n",
    "    hemi_dict = {}\n",
    "    \n",
    "    browser.visit(mars_hemisphere_url)\n",
    "    time.sleep(1)\n",
    "    hemispheres_html = browser.html\n",
    "    hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')\n",
    "    hemi_name_links = hemispheres_soup.find_all('a', class_='product-item')\n",
    "    hemi_name = hemi_name_links[i].text.strip('Enhanced')\n",
    "    \n",
    "    detail_links = browser.find_by_css('a.product-item')\n",
    "    detail_links[i].click()\n",
    "    time.sleep(1)\n",
    "    browser.find_link_by_text('Sample').first.click()\n",
    "    time.sleep(1)\n",
    "    browser.windows.current = browser.windows[-1]\n",
    "    hemi_img_html = browser.html\n",
    "    browser.windows.current = browser.windows[0]\n",
    "    browser.windows[-1].close()\n",
    "    \n",
    "    hemi_img_soup = BeautifulSoup(hemi_img_html, 'html.parser')\n",
    "    hemi_img_path = hemi_img_soup.find('img')['src']\n",
    "\n",
    "    print(hemi_name)\n",
    "    hemi_dict['title'] = hemi_name.strip()\n",
    "    \n",
    "    print(hemi_img_path)\n",
    "    hemi_dict['img_url'] = hemi_img_path\n",
    "\n",
    "    hemi_dicts.append(hemi_dict)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
