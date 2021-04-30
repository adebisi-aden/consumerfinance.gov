import os

from django.contrib.auth.models import User

from v1.models import LegacyNewsroomPage, ReusableText

octos = ["###", "# # #"]
splitter = "<p><center>"

en_disclaimer = ReusableText.objects.get(
    title="Press release disclaimer")  # pk44
es_disclaimer = ReusableText.objects.get(
    title="Press release disclaimer (Spanish)")  # pk 53
disclaimer_map = {
    'en': en_disclaimer,
    'es': es_disclaimer,
}
script_user_pk = os.getenv('SCRIPT_USER_PK', 9999)
user = User.objects.filter(id=script_user_pk).first()


def replace_disclaimers(pk=None):
    no_disclaimers = []
    fix_count = 0
    if pk:
        legacy_pages = LegacyNewsroomPage.objects.filter(pk=pk)
    else:
        legacy_pages = LegacyNewsroomPage.objects.all()

    for page in legacy_pages:
        snippet = disclaimer_map[page.language]
        stream_data = page.content.raw_data
        body = stream_data[0]['value']
        for octo in octos:
            if octo in body and splitter in body:
                page.content[0] = ('content', body.split(splitter)[0])
                page.content.append(('reusable_text', snippet.text))
                page.save()
                # page.save_revision(user=user).publish()
                fix_count += 1
            else:
                no_disclaimers.append((page.pk, page.url))
    print(
        "Fixed {} LegacyNewsroomPages and found "
        "these {} pages without disclaimers:\n"
        "{}".format(fix_count, len(no_disclaimers), "\n".join(no_disclaimers))
    )


def run(*args):
    if args:
        pk = args[0]
        replace_disclaimers(pk=pk)
    else:
        replace_disclaimers()
