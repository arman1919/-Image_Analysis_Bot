import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from ai_bot import fix_description

def image_analize(path):

    endpoint = "endpoint"
    key = "azure key"


    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    with open(path, "rb") as f:
        image_data = f.read()
        

    visual_features =[
            VisualFeatures.TAGS,
            VisualFeatures.OBJECTS,
            VisualFeatures.CAPTION,
            VisualFeatures.DENSE_CAPTIONS,
            VisualFeatures.READ,
            VisualFeatures.SMART_CROPS,
            VisualFeatures.PEOPLE,
        ]


    # Analyze all visual features from an image stream. This will be a synchronously (blocking) call.
    result = client.analyze(
        image_data=image_data,
        visual_features=visual_features,
        smart_crops_aspect_ratios=[0.9, 1.33],
        gender_neutral_caption=True,
        language="en"
    )


    text = '' 

    text += "Image analysis results:"



    if result.caption is not None:
        text += " Caption:"
        text += f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}"

    if result.dense_captions is not None:
        text += " Dense Captions:"
        for caption in result.dense_captions.list:
            text += f"   '{caption.text}', Confidence: {caption.confidence:.4f}"

    if result.read is not None and result.read.blocks:  # Check if blocks exist
        text += " Read:"
        for line in result.read.blocks[0].lines:
            text += f"   Line: '{line.text}' "
            for word in line.words:
                text += f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}"

    if result.tags is not None:
        text += " Tags:"
        for tag in result.tags.list:
            text +=f"   '{tag.name}', Confidence {tag.confidence:.4f}"

    if result.objects is not None:
        text += " Objects:"
        for object in result.objects.list:
            text += f"   '{object.tags[0].name}', Confidence: {object.tags[0].confidence:.4f}"

    if result.people is not None:
        text += " People:"
        for person in result.people.list:
            text += f" Confidence {person.confidence:.4f}"



    return fix_description(text)
