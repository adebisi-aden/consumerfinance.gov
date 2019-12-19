# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-19 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import v1.atomic_elements.molecules
import v1.blocks
import v1.models.snippets
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailsnippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0196_contact_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfgovpage',
            name='sidefoot',
            field=wagtail.wagtailcore.fields.StreamField([(b'call_to_action', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False)), (b'size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'regular', b'Regular'), (b'large', b'Large Primary')]))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'related_posts', wagtail.wagtailcore.blocks.StructBlock([(b'limit', wagtail.wagtailcore.blocks.CharBlock(default=b'3', help_text=b'This limit applies to EACH TYPE of post this module retrieves, not the total number of retrieved posts.')), (b'show_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'This toggles the heading and icon for the related types.', label=b'Show Heading and Icon?', required=False)), (b'header_title', wagtail.wagtailcore.blocks.CharBlock(default=b'Further reading', label=b'Slug Title')), (b'relate_posts', wagtail.wagtailcore.blocks.BooleanBlock(default=True, editable=False, label=b'Blog Posts', required=False)), (b'relate_newsroom', wagtail.wagtailcore.blocks.BooleanBlock(default=True, editable=False, label=b'Newsroom', required=False)), (b'relate_events', wagtail.wagtailcore.blocks.BooleanBlock(default=True, label=b'Events', required=False)), (b'specific_categories', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'Blog', ((b'At the CFPB', b'At the CFPB'), (b'Policy &amp; Compliance', b'Policy and compliance'), (b'Data, Research &amp; Reports', b'Data, research, and reports'), (b'Info for Consumers', b'Info for consumers'))), (b'Newsroom', ((b'Op-Ed', b'Op-ed'), (b'Press Release', b'Press release'), (b'Speech', b'Speech'), (b'Testimony', b'Testimony'), (b"Director's notebook", b"Director's notebook")))], required=False), required=False)), (b'and_filtering', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'If checked, related posts will only be pulled in if they match ALL topic tags set on this page. Otherwise, related posts can match any one topic tag.', label=b'Match all topic tags', required=False)), (b'alternate_view_more_url', wagtail.wagtailcore.blocks.CharBlock(help_text=b'By default, the "View more" link will go to the Activity Log, filtered based on the above parameters. Enter a URL in this field to override that link destination.', label=b'Alternate "View more" URL', required=False))])), (b'related_metadata', wagtail.wagtailcore.blocks.StructBlock([(b'slug', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'text', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'blob', wagtail.wagtailcore.blocks.RichTextBlock())], icon=b'pilcrow')), (b'list', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))], icon=b'list-ul')), (b'date', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'date', wagtail.wagtailcore.blocks.DateBlock())], icon=b'date')), (b'topics', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(default=b'Topics', max_length=100)), (b'show_topics', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False))], icon=b'tag')), (b'categories', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(default=b'Categories', max_length=100)), (b'show_categories', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False))], icon=b'list-ul'))])), (b'is_half_width', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))])), (b'email_signup', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(default=b'Stay informed', required=False)), (b'default_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label=b'Default heading style', required=False)), (b'text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), (b'gd_code', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label=b'GovDelivery code', required=False)), (b'disclaimer_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label=b'Privacy Act statement', required=False))])), (b'sidebar_contact', wagtail.wagtailcore.blocks.StructBlock([(b'contact', wagtail.wagtailsnippets.blocks.SnippetChooserBlock(b'v1.Contact')), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'Add a horizontal rule line to top of contact block.', required=False))])), (b'rss_feed', v1.atomic_elements.molecules.RSSFeed()), (b'social_media', wagtail.wagtailcore.blocks.StructBlock([(b'is_share_view', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'If unchecked, social media icons will link users to official CFPB accounts. Do not fill in any further fields.', label=b'Desired action: share this page', required=False)), (b'blurb', wagtail.wagtailcore.blocks.CharBlock(default=b"Look what I found on the CFPB's site!", help_text=b'Sets the tweet text, email subject line, and LinkedIn post text.', required=False)), (b'twitter_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom text for Twitter shares. If blank, will default to value of blurb field above.', max_length=100, required=False)), (b'twitter_related', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) A comma-separated list of accounts related to the content of the shared URL. Do not enter the  @ symbol. If blank, it will default to just "cfpb".', required=False)), (b'twitter_hashtags', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) A comma-separated list of hashtags to be appended to default tweet text.', required=False)), (b'twitter_lang', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Loads text components in the specified language, if other than English. E.g., use "es"  for Spanish. See https://dev.twitter.com/web/overview/languages for a list of supported language codes.', required=False)), (b'email_title', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom subject for email shares. If blank, will default to value of blurb field above.', required=False)), (b'email_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom text for email shares. If blank, will default to "Check out this page from the CFPB".', required=False)), (b'email_signature', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Adds a custom signature line to email shares. ', required=False)), (b'linkedin_title', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom title for LinkedIn shares. If blank, will default to value of blurb field above.', required=False)), (b'linkedin_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom text for LinkedIn shares.', required=False))])), (b'reusable_text', v1.blocks.ReusableTextChooserBlock(v1.models.snippets.ReusableText))], blank=True),
        ),
        migrations.AlterField(
            model_name='cfgovpagecategory',
            name='name',
            field=models.CharField(choices=[(b'Administrative adjudication docket', ((b'administrative-adjudication', b'Administrative adjudication'), (b'stipulation-and-constent-order', b'Stipulation and consent order'))), (b'Amicus Brief', ((b'us-supreme-court', b'U.S. Supreme Court'), (b'fed-circuit-court', b'Federal Circuit Court'), (b'fed-district-court', b'Federal District Court'), (b'state-court', b'State Court'))), (b'Blog', ((b'at-the-cfpb', b'At the CFPB'), (b'policy_compliance', b'Policy and compliance'), (b'data-research-reports', b'Data, research, and reports'), (b'info-for-consumers', b'Info for consumers'))), (b'Consumer Reporting Companies', ((b'nationwide', b'Nationwide'), (b'employment-screening', b'Employment screening'), (b'tenant-screening', b'Tenant screening'), (b'check-bank-screening', b'Check and bank screening'), (b'personal-property-insurance', b'Personal property insurance'), (b'medical', b'Medical'), (b'low-income-and-subprime', b'Low-income and subprime'), (b'supplementary-reports', b'Supplementary reports'), (b'utilities', b'Utilities'), (b'retail', b'Retail'), (b'gaming', b'Gaming'))), (b'Enforcement Action', ((b'fed-district-case', b'Federal district court case'), (b'administrative-adjudication-2', b'Administrative adjudication'), (b'stipulation-and-consent-order-2', b'Stipulation and consent order'), (b'civil-action', b'Civil Action'), (b'administrative-proceeding', b'Administrative Proceeding'))), (b'Final rule', ((b'interim-final-rule', b'Interim final rule'), (b'final-rule', b'Final rule'))), (b'FOIA Frequently Requested Record', ((b'report', b'Report'), (b'log', b'Log'), (b'record', b'Record'))), (b'Implementation Resource', ((b'compliance-aid', b'Compliance aid'), (b'official-guidance', b'Official guidance'))), (b'Newsroom', ((b'directors-notebook', b"Director's notebook"), (b'op-ed', b'Op-ed'), (b'press-release', b'Press release'), (b'speech', b'Speech'), (b'testimony', b'Testimony'))), (b'Notice and Opportunity for Comment', ((b'notice-proposed-rule', b'Advance notice of proposed rulemaking'), (b'proposed-rule', b'Proposed rule'), (b'interim-final-rule-2', b'Interim final rule'), (b'request-comment-info', b'Request for comment or information'), (b'proposed-policy', b'Proposed policy'), (b'intent-preempt-determ', b'Intent to make preemption determination'), (b'info-collect-activity', b'Information collection activities'), (b'notice-privacy-act', b'Notice related to Privacy Act'))), (b'Research Report', ((b'consumer-complaint', b'Consumer complaint'), (b'super-highlight', b'Supervisory Highlights'), (b'data-point', b'Data point'), (b'industry-markets', b'Industry and markets'), (b'consumer-edu-empower', b'Consumer education and empowerment'), (b'to-congress', b'To Congress'))), (b'Rule Under Development', ((b'notice-proposed-rule-2', b'Advance notice of proposed rulemaking'), (b'proposed-rule-2', b'Proposed rule'))), (b'Story', ((b'auto-loans', b'Auto loans'), (b'bank-accts-services', b'Bank accounts and services'), (b'credit-cards', b'Credit cards'), (b'credit-reports-scores', b'Credit reports and scores'), (b'debt-collection', b'Debt collection'), (b'money-transfers', b'Money transfers'), (b'mortgages', b'Mortgages'), (b'payday-loans', b'Payday loans'), (b'prepaid-cards', b'Prepaid cards'), (b'student-loans', b'Student loans')))], max_length=255),
        ),
    ]
