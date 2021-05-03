import os

from django.contrib.auth.models import User

from v1.models import LegacyNewsroomPage, ReusableText

from wagtail.core.models import Page

octos = ["###", "# # #"]

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

legacy_string = """The Consumer Financial Protection Bureau is a 21st century agency that helps consumer finance markets work by making rules more effective, by consistently and fairly enforcing those rules, and by empowering consumers to take more control over their economic lives."""


def replace_disclaimers(pk=None):
    no_octos = []
    no_splitters = []
    fix_count = 0
    if pk:
        legacy_pages = LegacyNewsroomPage.objects.filter(pk=pk)
    else:
        legacy_pages = LegacyNewsroomPage.objects.filter(live=True)

    for page in legacy_pages:
        snippet = disclaimer_map[page.language]
        stream_data = page.content.raw_data
        # Handle pages with 2 content fields (arbitration notices + content)
        if len(stream_data) == 2:
            i = 1
        else:
            i = 0
        body = stream_data[i].get('value')
        # skip pages that have no octos or have been fixed with a snippet
        if isinstance(body, int) or (octos[0] not in body and octos[1] not in body):  # noqa
            no_octos.append(f"page pk: {page.pk}, url: {page.url}")
            continue
        for octo in octos:
            if octo not in body:
                continue
            splitters = [
                f"<p><center>{octo}",
                f"<center>{octo}",
                f"<p>{octo}",
                f"<p><center><strong>{octo}",
                f'<p align="center">{octo}',
                f'<p align="center"><i>{octo}',
                f'<p align="center"><span>{octo}'
            ]
            new_content = None
            for splitter in splitters:
                if splitter in body:
                    new_content = body.split(splitter)[0]
                    break
            if new_content is None:
                no_splitters.append(
                    f"No splitter found for page pk {page.pk}, url: {page.url}"
                )
            else:
                page.content[i] = ('content', new_content)
                page.content.append(('reusable_text', snippet))
                page.save_revision(user=user).publish()
                fix_count += 1

    print(
        "Checked {} LegacyNewsroomPages, "
        "fixed {} and found {} pages without any octos:\n"
        "{}".format(
            legacy_pages.count(),
            fix_count,
            len(no_octos),
            "\n".join(no_octos))
    )
    if no_splitters:
        print(
            "Found these entries with no splitters:\n"
            "{}".format("\n".join(no_splitters))
        )


def run(*args):
    if args:
        pk = args[0]
        replace_disclaimers(pk=pk)
    else:
        replace_disclaimers()
