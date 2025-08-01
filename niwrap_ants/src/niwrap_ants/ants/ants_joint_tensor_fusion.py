# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTS_JOINT_TENSOR_FUSION_METADATA = Metadata(
    id="cb4fe8a4aace4f1fb43afc13b52fb4d917f9af4c.boutiques",
    name="antsJointTensorFusion",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


AntsJointTensorFusionParameters = typing.TypedDict('AntsJointTensorFusionParameters', {
    "__STYXTYPE__": typing.Literal["antsJointTensorFusion"],
    "dimensionality": typing.NotRequired[typing.Literal[2, 3, 4] | None],
    "target_image": list[str],
    "atlas_image": list[str],
    "atlas_segmentation": InputPathType,
    "alpha": typing.NotRequired[float | None],
    "beta": typing.NotRequired[float | None],
    "retain_label_posterior_images": typing.NotRequired[typing.Literal[0, 1] | None],
    "retain_atlas_voting_images": typing.NotRequired[typing.Literal[0, 1] | None],
    "constrain_nonnegative": typing.NotRequired[typing.Literal[0, 1] | None],
    "log_euclidean": typing.NotRequired[typing.Literal[0, 1] | None],
    "patch_radius": typing.NotRequired[str | None],
    "patch_metric": typing.NotRequired[typing.Literal["PC", "MSQ"] | None],
    "search_radius": typing.NotRequired[str | None],
    "exclusion_image": typing.NotRequired[str | None],
    "mask_image": typing.NotRequired[InputPathType | None],
    "output": str,
    "verbose": typing.NotRequired[typing.Literal[0, 1] | None],
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
        "antsJointTensorFusion": ants_joint_tensor_fusion_cargs,
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
        "antsJointTensorFusion": ants_joint_tensor_fusion_outputs,
    }.get(t)


class AntsJointTensorFusionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_joint_tensor_fusion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_fusion_image: OutputPathType
    """The label fusion image output."""
    intensity_fusion_image: OutputPathType
    """The intensity fusion image output."""
    label_posterior_probability_image: OutputPathType
    """The label posterior probability images."""
    atlas_voting_weight_image: OutputPathType
    """The atlas voting weight images."""


def ants_joint_tensor_fusion_params(
    target_image: list[str],
    atlas_image: list[str],
    atlas_segmentation: InputPathType,
    output: str,
    dimensionality: typing.Literal[2, 3, 4] | None = None,
    alpha: float | None = 0.1,
    beta: float | None = 2.0,
    retain_label_posterior_images: typing.Literal[0, 1] | None = None,
    retain_atlas_voting_images: typing.Literal[0, 1] | None = None,
    constrain_nonnegative: typing.Literal[0, 1] | None = None,
    log_euclidean: typing.Literal[0, 1] | None = None,
    patch_radius: str | None = None,
    patch_metric: typing.Literal["PC", "MSQ"] | None = None,
    search_radius: str | None = None,
    exclusion_image: str | None = None,
    mask_image: InputPathType | None = None,
    verbose: typing.Literal[0, 1] | None = None,
) -> AntsJointTensorFusionParameters:
    """
    Build parameters.
    
    Args:
        target_image: The target image (or multimodal target images) assumed to\
            be aligned to a common image domain.
        atlas_image: The atlas image (or multimodal atlas images) assumed to be\
            aligned to a common image domain.
        atlas_segmentation: The atlas segmentation images. For performing label\
            fusion the number of specified segmentations should be identical to the\
            number of atlas image sets.
        output: The output is the intensity and/or label fusion image.\
            Additional optional outputs include the label posterior probability\
            images and the atlas voting weight images.
        dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, the program tries to\
            infer the dimensionality from the input image.
        alpha: Regularization term added to matrix Mx for calculating the\
            inverse. Default = 0.1.
        beta: Exponent for mapping intensity difference to the joint error.\
            Default = 2.0.
        retain_label_posterior_images: Retain label posterior probability\
            images. Requires atlas segmentations to be specified. Default = false.
        retain_atlas_voting_images: Retain atlas voting images. Default = false.
        constrain_nonnegative: Constrain solution to non-negative weights.
        log_euclidean: Use log Euclidean space for tensor math.
        patch_radius: Patch radius for similarity measures. Default = 2x2x2.
        patch_metric: Metric to be used in determining the most similar\
            neighborhood patch. Options include Pearson's correlation (PC) and mean\
            squares (MSQ). Default = PC.
        search_radius: Search radius for similarity measures. Default = 3x3x3.
        exclusion_image: Specify an exclusion region for the given label.
        mask_image: If a mask image is specified, fusion is only performed in\
            the mask region.
        verbose: Verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsJointTensorFusion",
        "target_image": target_image,
        "atlas_image": atlas_image,
        "atlas_segmentation": atlas_segmentation,
        "output": output,
    }
    if dimensionality is not None:
        params["dimensionality"] = dimensionality
    if alpha is not None:
        params["alpha"] = alpha
    if beta is not None:
        params["beta"] = beta
    if retain_label_posterior_images is not None:
        params["retain_label_posterior_images"] = retain_label_posterior_images
    if retain_atlas_voting_images is not None:
        params["retain_atlas_voting_images"] = retain_atlas_voting_images
    if constrain_nonnegative is not None:
        params["constrain_nonnegative"] = constrain_nonnegative
    if log_euclidean is not None:
        params["log_euclidean"] = log_euclidean
    if patch_radius is not None:
        params["patch_radius"] = patch_radius
    if patch_metric is not None:
        params["patch_metric"] = patch_metric
    if search_radius is not None:
        params["search_radius"] = search_radius
    if exclusion_image is not None:
        params["exclusion_image"] = exclusion_image
    if mask_image is not None:
        params["mask_image"] = mask_image
    if verbose is not None:
        params["verbose"] = verbose
    return params


def ants_joint_tensor_fusion_cargs(
    params: AntsJointTensorFusionParameters,
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
    cargs.append("antsJointTensorFusion")
    if params.get("dimensionality") is not None:
        cargs.extend([
            "--image-dimensionality",
            str(params.get("dimensionality"))
        ])
    cargs.extend([
        "-t",
        ",".join(params.get("target_image"))
    ])
    cargs.extend([
        "-g",
        ",".join(params.get("atlas_image"))
    ])
    cargs.extend([
        "-l",
        execution.input_file(params.get("atlas_segmentation"))
    ])
    if params.get("alpha") is not None:
        cargs.extend([
            "-a",
            str(params.get("alpha"))
        ])
    if params.get("beta") is not None:
        cargs.extend([
            "-b",
            str(params.get("beta"))
        ])
    if params.get("retain_label_posterior_images") is not None:
        cargs.extend([
            "-r",
            str(params.get("retain_label_posterior_images"))
        ])
    if params.get("retain_atlas_voting_images") is not None:
        cargs.extend([
            "-f",
            str(params.get("retain_atlas_voting_images"))
        ])
    if params.get("constrain_nonnegative") is not None:
        cargs.extend([
            "-c",
            str(params.get("constrain_nonnegative"))
        ])
    if params.get("log_euclidean") is not None:
        cargs.extend([
            "-u",
            str(params.get("log_euclidean"))
        ])
    if params.get("patch_radius") is not None:
        cargs.extend([
            "-p",
            params.get("patch_radius")
        ])
    if params.get("patch_metric") is not None:
        cargs.extend([
            "-m",
            params.get("patch_metric")
        ])
    if params.get("search_radius") is not None:
        cargs.extend([
            "-s",
            params.get("search_radius")
        ])
    if params.get("exclusion_image") is not None:
        cargs.extend([
            "-e",
            params.get("exclusion_image")
        ])
    if params.get("mask_image") is not None:
        cargs.extend([
            "-x",
            execution.input_file(params.get("mask_image"))
        ])
    cargs.extend([
        "-o",
        params.get("output")
    ])
    if params.get("verbose") is not None:
        cargs.extend([
            "-v",
            str(params.get("verbose"))
        ])
    return cargs


def ants_joint_tensor_fusion_outputs(
    params: AntsJointTensorFusionParameters,
    execution: Execution,
) -> AntsJointTensorFusionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsJointTensorFusionOutputs(
        root=execution.output_file("."),
        label_fusion_image=execution.output_file(params.get("output") + "_LabelFusion.nii.gz"),
        intensity_fusion_image=execution.output_file(params.get("output") + "_IntensityFusion.nii.gz"),
        label_posterior_probability_image=execution.output_file(params.get("output") + "_LabelPosterior.nii.gz"),
        atlas_voting_weight_image=execution.output_file(params.get("output") + "_AtlasVoting.nii.gz"),
    )
    return ret


def ants_joint_tensor_fusion_execute(
    params: AntsJointTensorFusionParameters,
    execution: Execution,
) -> AntsJointTensorFusionOutputs:
    """
    antsJointTensorFusion is an image fusion algorithm developed by Hongzhi Wang and
    Paul Yushkevich which won segmentation challenges at MICCAI 2012 and MICCAI
    2013. The original label fusion framework was extended to accommodate
    intensities by Brian Avants. This implementation is based on the original
    ITK-style implementation and ANTsR implementation.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsJointTensorFusionOutputs`).
    """
    params = execution.params(params)
    cargs = ants_joint_tensor_fusion_cargs(params, execution)
    ret = ants_joint_tensor_fusion_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_joint_tensor_fusion(
    target_image: list[str],
    atlas_image: list[str],
    atlas_segmentation: InputPathType,
    output: str,
    dimensionality: typing.Literal[2, 3, 4] | None = None,
    alpha: float | None = 0.1,
    beta: float | None = 2.0,
    retain_label_posterior_images: typing.Literal[0, 1] | None = None,
    retain_atlas_voting_images: typing.Literal[0, 1] | None = None,
    constrain_nonnegative: typing.Literal[0, 1] | None = None,
    log_euclidean: typing.Literal[0, 1] | None = None,
    patch_radius: str | None = None,
    patch_metric: typing.Literal["PC", "MSQ"] | None = None,
    search_radius: str | None = None,
    exclusion_image: str | None = None,
    mask_image: InputPathType | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> AntsJointTensorFusionOutputs:
    """
    antsJointTensorFusion is an image fusion algorithm developed by Hongzhi Wang and
    Paul Yushkevich which won segmentation challenges at MICCAI 2012 and MICCAI
    2013. The original label fusion framework was extended to accommodate
    intensities by Brian Avants. This implementation is based on the original
    ITK-style implementation and ANTsR implementation.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        target_image: The target image (or multimodal target images) assumed to\
            be aligned to a common image domain.
        atlas_image: The atlas image (or multimodal atlas images) assumed to be\
            aligned to a common image domain.
        atlas_segmentation: The atlas segmentation images. For performing label\
            fusion the number of specified segmentations should be identical to the\
            number of atlas image sets.
        output: The output is the intensity and/or label fusion image.\
            Additional optional outputs include the label posterior probability\
            images and the atlas voting weight images.
        dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, the program tries to\
            infer the dimensionality from the input image.
        alpha: Regularization term added to matrix Mx for calculating the\
            inverse. Default = 0.1.
        beta: Exponent for mapping intensity difference to the joint error.\
            Default = 2.0.
        retain_label_posterior_images: Retain label posterior probability\
            images. Requires atlas segmentations to be specified. Default = false.
        retain_atlas_voting_images: Retain atlas voting images. Default = false.
        constrain_nonnegative: Constrain solution to non-negative weights.
        log_euclidean: Use log Euclidean space for tensor math.
        patch_radius: Patch radius for similarity measures. Default = 2x2x2.
        patch_metric: Metric to be used in determining the most similar\
            neighborhood patch. Options include Pearson's correlation (PC) and mean\
            squares (MSQ). Default = PC.
        search_radius: Search radius for similarity measures. Default = 3x3x3.
        exclusion_image: Specify an exclusion region for the given label.
        mask_image: If a mask image is specified, fusion is only performed in\
            the mask region.
        verbose: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsJointTensorFusionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_JOINT_TENSOR_FUSION_METADATA)
    params = ants_joint_tensor_fusion_params(
        dimensionality=dimensionality,
        target_image=target_image,
        atlas_image=atlas_image,
        atlas_segmentation=atlas_segmentation,
        alpha=alpha,
        beta=beta,
        retain_label_posterior_images=retain_label_posterior_images,
        retain_atlas_voting_images=retain_atlas_voting_images,
        constrain_nonnegative=constrain_nonnegative,
        log_euclidean=log_euclidean,
        patch_radius=patch_radius,
        patch_metric=patch_metric,
        search_radius=search_radius,
        exclusion_image=exclusion_image,
        mask_image=mask_image,
        output=output,
        verbose=verbose,
    )
    return ants_joint_tensor_fusion_execute(params, execution)


__all__ = [
    "ANTS_JOINT_TENSOR_FUSION_METADATA",
    "AntsJointTensorFusionOutputs",
    "AntsJointTensorFusionParameters",
    "ants_joint_tensor_fusion",
    "ants_joint_tensor_fusion_params",
]
