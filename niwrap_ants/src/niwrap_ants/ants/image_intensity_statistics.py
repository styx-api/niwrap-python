# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMAGE_INTENSITY_STATISTICS_METADATA = Metadata(
    id="ba7ab9e8e494076bff274459f3f86dfd1563d5d9.boutiques",
    name="ImageIntensityStatistics",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


ImageIntensityStatisticsParameters = typing.TypedDict('ImageIntensityStatisticsParameters', {
    "__STYXTYPE__": typing.Literal["ImageIntensityStatistics"],
    "image_dimension": int,
    "input_image": InputPathType,
    "label_image": typing.NotRequired[InputPathType | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "ImageIntensityStatistics": image_intensity_statistics_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "ImageIntensityStatistics": image_intensity_statistics_outputs,
    }.get(t)


class ImageIntensityStatisticsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `image_intensity_statistics(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    intensity_statistics: OutputPathType
    """The output file containing intensity statistics."""


def image_intensity_statistics_params(
    image_dimension: int,
    input_image: InputPathType,
    label_image: InputPathType | None = None,
) -> ImageIntensityStatisticsParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: The dimensionality of the image (e.g., 2D, 3D).
        input_image: The input image for which intensity statistics will be\
            computed.
        label_image: An optional label image which defines regions of interest.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ImageIntensityStatistics",
        "image_dimension": image_dimension,
        "input_image": input_image,
    }
    if label_image is not None:
        params["label_image"] = label_image
    return params


def image_intensity_statistics_cargs(
    params: ImageIntensityStatisticsParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("ImageIntensityStatistics")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("input_image")))
    if params.get("label_image") is not None:
        cargs.append(execution.input_file(params.get("label_image")))
    return cargs


def image_intensity_statistics_outputs(
    params: ImageIntensityStatisticsParameters,
    execution: Execution,
) -> ImageIntensityStatisticsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImageIntensityStatisticsOutputs(
        root=execution.output_file("."),
        intensity_statistics=execution.output_file("intensity_statistics.txt"),
    )
    return ret


def image_intensity_statistics_execute(
    params: ImageIntensityStatisticsParameters,
    execution: Execution,
) -> ImageIntensityStatisticsOutputs:
    """
    This tool computes intensity statistics of an input image, optionally given a
    label image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImageIntensityStatisticsOutputs`).
    """
    params = execution.params(params)
    cargs = image_intensity_statistics_cargs(params, execution)
    ret = image_intensity_statistics_outputs(params, execution)
    execution.run(cargs)
    return ret


def image_intensity_statistics(
    image_dimension: int,
    input_image: InputPathType,
    label_image: InputPathType | None = None,
    runner: Runner | None = None,
) -> ImageIntensityStatisticsOutputs:
    """
    This tool computes intensity statistics of an input image, optionally given a
    label image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the image (e.g., 2D, 3D).
        input_image: The input image for which intensity statistics will be\
            computed.
        label_image: An optional label image which defines regions of interest.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImageIntensityStatisticsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMAGE_INTENSITY_STATISTICS_METADATA)
    params = image_intensity_statistics_params(
        image_dimension=image_dimension,
        input_image=input_image,
        label_image=label_image,
    )
    return image_intensity_statistics_execute(params, execution)


__all__ = [
    "IMAGE_INTENSITY_STATISTICS_METADATA",
    "ImageIntensityStatisticsOutputs",
    "ImageIntensityStatisticsParameters",
    "image_intensity_statistics",
    "image_intensity_statistics_params",
]
