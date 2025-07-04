from wagtail.blocks import (
    BlockQuoteBlock,
    CharBlock,
    ChoiceBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    URLBlock
)
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class DocumentBlock(StructBlock):
    document = DocumentChooserBlock(required=True),
    title = CharBlock(required=True)

    class Meta:
        icon = "doc-full"
        template = "webikwa257/blocks/document_block.html"


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    alt = CharBlock(required=True)
    link = URLBlock(required=False)

    class Meta:
        icon = "image"
        template = "webikwa257/blocks/image_block.html"

class ExternalImageBlock(StructBlock):
    url = URLBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    alt = CharBlock(required=True)
    link = URLBlock(required=False)

    class Meta:
        icon = "image"
        template = "webikwa257/blocks/external_image_block.html"


class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
            ("h5", "H5"),
            ("h6", "H6"),

        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "webikwa257/blocks/heading_block.html"



class BaseStreamBlock(StreamBlock):
    paragraph_block = RichTextBlock(icon="pilcrow", features=["link","bold","italic","ol","ul"])
    heading_block = HeadingBlock()
    document_block = DocumentChooserBlock()
    quote_block = BlockQuoteBlock()
    image_block = ImageBlock()
    external_image_block = ExternalImageBlock()
    embed_block = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )
    table = TableBlock()

class BodyStreamBlock(BaseStreamBlock):
    pass
