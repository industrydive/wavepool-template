code_reviews = [
    # {
    #     'title': 'Site front page',
    #     'description': 'There are several bugs on the front page of the Wavepool site. Fix these bugs by editing the front_page.html template file and the front_page view in views.py. Submit a pull request for a branch titled "yourlastname_yourfirstname_front_page_fixes"',  # noqa
    #     'acceptance_criteria': [
    #         'The newspost designated as the cover story should appear in the cover story box',
    #         'The 3 most recent stories, excluding the cover story, should be displayed under "top stories", ordered by most recent first',  # noqa
    #         'All news posts that do not appear as the cover story or as top stories should be listed in the archive, ordered by most recent first',  # noqa
    #         'Newspost teasers should be properly rendered as HTML',
    #     ],
    #     'pull_request': 'https://github.com/industrydive/wavepool/pull/2',
    # },
]

code_prompts = [
    {
        'title': 'Customizable News Post Ads',
        'description': '''
        The sales team currently sells a single advertisement to a client for the whole site.
        The HTML for this ad is periodically updated manually via engineering team support tickets.
        The Sales Team wants the ability to create their own ads using the CMS and assign them to specific news posts
        in order to maximize revenue. The existing ads can be found in <code>advertising/__init__.py</code>
        ''',
        'acceptance_criteria': [
            'A Sales Team member can access a set of standard admin pages in the CMS to create advertisements',
            'For each advertisement they should be able to upload a client logo, a link that the ad should open to, and the ad\'s text',  # noqa
            'Each advertisement should appear on the news post that it is sold for',
            'The Sales Team might sell more than one news post slot to a client at a time, so they should be able to set a single ad to multiple posts',  # noqa
        ],
    },
    {
        'title': 'Cover Story CMS Functionality',
        'description': '''
            Currently, there is no way to stop a CMS user from setting more than one story as the cover story. There is
            also nothing that alerts the Editorial Team if no story is currently set as a cover story.
            The front page template is not set up to allow for these situations. The Editorial team has requested a
            couple of features to address this user experience:</p>
            <ol>
            <li>Update the CMS so that if a news post is set as the cover story, other news posts that are set as the
            cover story get un-set.</li>
            <li>Add an alert message on the news post list page so that Editors can see when when there is no current
            cover story.</li>
            </ol>
        ''',
        'acceptance_criteria': [
            'Only one story can be saved as the cover story using the <code>is_cover_story</code> field',
        ],
        'relevant_screenshots': [
            'no-cover-story-alert.png',
        ]
    },
    {
        'title': 'Bug in News Post teaser',
        'description': '''
            There is a logical error in the handling of News Post teaser field - the current logic uses the first 150
            characters of the News Post body as the teaser. If this part of the News Post contains HTML tags that are
            not closed by the end of the character cut off, then it can mess up the HTML of the whole page. An example
            of this can be seen with the News Post "Regeneron antibody cuts risk of COVID-19 death in UK study". You
            can reproduce the behavior by setting this News Post to <code>active</code> and viewing the Front Page or
            the Archive Page. Design and implement a solution so that News Post teasers can be custom set by editors
            or so that they print safely when included in feed lists.
        ''',
        'acceptance_criteria': [
            'News posts with HTML tags do not disrupt the HTML structure of the wavepool site'
        ],
        'relevant_screenshots': [
            'teaser-html-bug.png',
        ]
    },
]
