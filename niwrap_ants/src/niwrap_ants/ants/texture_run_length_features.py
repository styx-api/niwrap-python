# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TEXTURE_RUN_LENGTH_FEATURES_METADATA = Metadata(
    id="99c3089b305255bec7d6249a4c2fc94894071c52.boutiques",
    name="TextureRunLengthFeatures",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


TextureRunLengthFeaturesParameters = typing.TypedDict('TextureRunLengthFeaturesParameters', {
    "__STYXTYPE__": typing.Literal["TextureRunLengthFeatures"],
    "image_dimension": int,
    "input_image": InputPathType,
    "number_of_bins_per_axis": typing.NotRequired[int | None],
    "mask_image": typing.NotRequired[InputPathType | None],
    "mask_label": typing.NotRequired[int | None],
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
        "TextureRunLengthFeatures": texture_run_length_features_cargs,
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
        "TextureRunLengthFeatures": texture_run_length_features_outputs,
    }.get(t)


class TextureRunLengthFeaturesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `texture_run_length_features(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    short_run_emphasis: OutputPathType
    """Output feature: Short Run Emphasis."""
    long_run_emphasis: OutputPathType
    """Output feature: Long Run Emphasis."""
    grey_level_nonuniformity: OutputPathType
    """Output feature: Grey Level Nonuniformity."""
    run_length_nonuniformity: OutputPathType
    """Output feature: Run Length Nonuniformity."""
    low_grey_level_run_emphasis: OutputPathType
    """Output feature: Low Grey Level Run Emphasis."""
    high_grey_level_run_emphasis: OutputPathType
    """Output feature: High Grey Level Run Emphasis."""
    short_run_low_grey_level_emphasis: OutputPathType
    """Output feature: Short Run Low Grey Level Emphasis."""
    short_run_high_grey_level_emphasis: OutputPathType
    """Output feature: Short Run High Grey Level Emphasis."""
    long_run_low_grey_level_emphasis: OutputPathType
    """Output feature: Long Run Low Grey Level Emphasis."""
    long_run_high_grey_level_emphasis: OutputPathType
    """Output feature: Long Run High Grey Level Emphasis."""


def texture_run_length_features_params(
    image_dimension: int,
    input_image: InputPathType,
    number_of_bins_per_axis: int | None = 256,
    mask_image: InputPathType | None = None,
    mask_label: int | None = 1,
) -> TextureRunLengthFeaturesParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: The dimensionality of the input image.
        input_image: The path to the input image file.
        number_of_bins_per_axis: The number of bins per axis for the histogram.
        mask_image: The path to the mask image file.
        mask_label: The label value in the mask image to be used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "TextureRunLengthFeatures",
        "image_dimension": image_dimension,
        "input_image": input_image,
    }
    if number_of_bins_per_axis is not None:
        params["number_of_bins_per_axis"] = number_of_bins_per_axis
    if mask_image is not None:
        params["mask_image"] = mask_image
    if mask_label is not None:
        params["mask_label"] = mask_label
    return params


def texture_run_length_features_cargs(
    params: TextureRunLengthFeaturesParameters,
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
    cargs.append("TextureRunLengthFeatures")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("input_image")))
    if params.get("number_of_bins_per_axis") is not None:
        cargs.append(str(params.get("number_of_bins_per_axis")))
    if params.get("mask_image") is not None:
        cargs.append(execution.input_file(params.get("mask_image")))
    if params.get("mask_label") is not None:
        cargs.append(str(params.get("mask_label")))
    return cargs


def texture_run_length_features_outputs(
    params: TextureRunLengthFeaturesParameters,
    execution: Execution,
) -> TextureRunLengthFeaturesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TextureRunLengthFeaturesOutputs(
        root=execution.output_file("."),
        short_run_emphasis=execution.output_file("short_run_emphasis.csv"),
        long_run_emphasis=execution.output_file("long_run_emphasis.csv"),
        grey_level_nonuniformity=execution.output_file("grey_level_nonuniformity.csv"),
        run_length_nonuniformity=execution.output_file("run_length_nonuniformity.csv"),
        low_grey_level_run_emphasis=execution.output_file("low_grey_level_run_emphasis.csv"),
        high_grey_level_run_emphasis=execution.output_file("high_grey_level_run_emphasis.csv"),
        short_run_low_grey_level_emphasis=execution.output_file("short_run_low_grey_level_emphasis.csv"),
        short_run_high_grey_level_emphasis=execution.output_file("short_run_high_grey_level_emphasis.csv"),
        long_run_low_grey_level_emphasis=execution.output_file("long_run_low_grey_level_emphasis.csv"),
        long_run_high_grey_level_emphasis=execution.output_file("long_run_high_grey_level_emphasis.csv"),
    )
    return ret


def texture_run_length_features_execute(
    params: TextureRunLengthFeaturesParameters,
    execution: Execution,
) -> TextureRunLengthFeaturesOutputs:
    """
    A tool to calculate texture run length features on an input image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TextureRunLengthFeaturesOutputs`).
    """
    params = execution.params(params)
    cargs = texture_run_length_features_cargs(params, execution)
    ret = texture_run_length_features_outputs(params, execution)
    execution.run(cargs)
    return ret


def texture_run_length_features(
    image_dimension: int,
    input_image: InputPathType,
    number_of_bins_per_axis: int | None = 256,
    mask_image: InputPathType | None = None,
    mask_label: int | None = 1,
    runner: Runner | None = None,
) -> TextureRunLengthFeaturesOutputs:
    """
    A tool to calculate texture run length features on an input image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the input image.
        input_image: The path to the input image file.
        number_of_bins_per_axis: The number of bins per axis for the histogram.
        mask_image: The path to the mask image file.
        mask_label: The label value in the mask image to be used.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TextureRunLengthFeaturesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TEXTURE_RUN_LENGTH_FEATURES_METADATA)
    params = texture_run_length_features_params(
        image_dimension=image_dimension,
        input_image=input_image,
        number_of_bins_per_axis=number_of_bins_per_axis,
        mask_image=mask_image,
        mask_label=mask_label,
    )
    return texture_run_length_features_execute(params, execution)


__all__ = [
    "TEXTURE_RUN_LENGTH_FEATURES_METADATA",
    "TextureRunLengthFeaturesOutputs",
    "TextureRunLengthFeaturesParameters",
    "texture_run_length_features",
    "texture_run_length_features_params",
]
