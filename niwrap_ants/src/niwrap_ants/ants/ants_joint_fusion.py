# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTS_JOINT_FUSION_METADATA = Metadata(
    id="ead66a78d253bbef7d330bdf2dee14d07d54b7fe.boutiques",
    name="antsJointFusion",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


AntsJointFusionParameters = typing.TypedDict('AntsJointFusionParameters', {
    "__STYXTYPE__": typing.Literal["antsJointFusion"],
    "image_dimensionality": typing.NotRequired[typing.Literal[2, 3, 4] | None],
    "target_image": list[InputPathType],
    "atlas_image": list[InputPathType],
    "atlas_segmentation": InputPathType,
    "alpha": typing.NotRequired[float | None],
    "beta": typing.NotRequired[float | None],
    "constrain_nonnegative": typing.NotRequired[typing.Literal[0, 1] | None],
    "patch_radius": typing.NotRequired[str | None],
    "patch_metric": typing.NotRequired[typing.Literal["PC", "MSQ"] | None],
    "search_radius": typing.NotRequired[str | None],
    "exclusion_image": typing.NotRequired[InputPathType | None],
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
        "antsJointFusion": ants_joint_fusion_cargs,
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
        "antsJointFusion": ants_joint_fusion_outputs,
    }.get(t)


class AntsJointFusionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_joint_fusion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_fusion_image: OutputPathType
    """The output label fusion image."""
    intensity_fusion_image: OutputPathType
    """The output intensity fusion image format."""
    label_posterior_probability_image: OutputPathType
    """The output label posterior probability image format."""
    atlas_voting_weight_image: OutputPathType
    """The output atlas voting weight image format."""


def ants_joint_fusion_params(
    target_image: list[InputPathType],
    atlas_image: list[InputPathType],
    atlas_segmentation: InputPathType,
    output: str,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    alpha: float | None = 0.1,
    beta: float | None = 2.0,
    constrain_nonnegative: typing.Literal[0, 1] | None = None,
    patch_radius: str | None = "2x2x2",
    patch_metric: typing.Literal["PC", "MSQ"] | None = "PC",
    search_radius: str | None = "3x3x3",
    exclusion_image: InputPathType | None = None,
    mask_image: InputPathType | None = None,
    verbose: typing.Literal[0, 1] | None = None,
) -> AntsJointFusionParameters:
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
        image_dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, the program tries to\
            infer the dimensionality from the input image.
        alpha: Regularization term added to matrix Mx for calculating the\
            inverse. Default = 0.1.
        beta: Exponent for mapping intensity difference to the joint error.\
            Default = 2.0.
        constrain_nonnegative: Constrain solution to non-negative weights.
        patch_radius: Patch radius for similarity measures. Default = 2x2x2.
        patch_metric: Metric to be used in determining the most similar\
            neighborhood patch. Options include Pearson's correlation (PC) and mean\
            squares (MSQ). Default = PC (Pearson correlation).
        search_radius: Search radius for similarity measures. Default = 3x3x3.\
            One can also specify an image where the value at the voxel specifies\
            the isotropic search radius at that voxel.
        exclusion_image: Specify an exclusion region for the given label.
        mask_image: If a mask image is specified, fusion is only performed in\
            the mask region.
        verbose: Verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsJointFusion",
        "target_image": target_image,
        "atlas_image": atlas_image,
        "atlas_segmentation": atlas_segmentation,
        "output": output,
    }
    if image_dimensionality is not None:
        params["image_dimensionality"] = image_dimensionality
    if alpha is not None:
        params["alpha"] = alpha
    if beta is not None:
        params["beta"] = beta
    if constrain_nonnegative is not None:
        params["constrain_nonnegative"] = constrain_nonnegative
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


def ants_joint_fusion_cargs(
    params: AntsJointFusionParameters,
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
    cargs.append("antsJointFusion")
    if params.get("image_dimensionality") is not None:
        cargs.extend([
            "--image-dimensionality",
            str(params.get("image_dimensionality"))
        ])
    cargs.extend([
        "--target-image",
        *[execution.input_file(f) for f in params.get("target_image")]
    ])
    cargs.extend([
        "--atlas-image",
        *[execution.input_file(f) for f in params.get("atlas_image")]
    ])
    cargs.extend([
        "--atlas-segmentation",
        execution.input_file(params.get("atlas_segmentation"))
    ])
    if params.get("alpha") is not None:
        cargs.extend([
            "--alpha",
            str(params.get("alpha"))
        ])
    if params.get("beta") is not None:
        cargs.extend([
            "--beta",
            str(params.get("beta"))
        ])
    if params.get("constrain_nonnegative") is not None:
        cargs.extend([
            "--constrain-nonnegative",
            str(params.get("constrain_nonnegative"))
        ])
    if params.get("patch_radius") is not None:
        cargs.extend([
            "--patch-radius",
            params.get("patch_radius")
        ])
    if params.get("patch_metric") is not None:
        cargs.extend([
            "--patch-metric",
            params.get("patch_metric")
        ])
    if params.get("search_radius") is not None:
        cargs.extend([
            "--search-radius",
            params.get("search_radius")
        ])
    if params.get("exclusion_image") is not None:
        cargs.extend([
            "--exclusion-image",
            execution.input_file(params.get("exclusion_image"))
        ])
    if params.get("mask_image") is not None:
        cargs.extend([
            "--mask-image",
            execution.input_file(params.get("mask_image"))
        ])
    cargs.extend([
        "--output",
        params.get("output")
    ])
    if params.get("verbose") is not None:
        cargs.extend([
            "--verbose",
            str(params.get("verbose"))
        ])
    return cargs


def ants_joint_fusion_outputs(
    params: AntsJointFusionParameters,
    execution: Execution,
) -> AntsJointFusionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsJointFusionOutputs(
        root=execution.output_file("."),
        label_fusion_image=execution.output_file("[LABELFUSIONIMAGE]"),
        intensity_fusion_image=execution.output_file("[INTENSITYFUSIONIMAGEFILENAMEFORMAT]"),
        label_posterior_probability_image=execution.output_file("[LABELPOSTERIORPROBABILITYIMAGEFILENAMEFORMAT]"),
        atlas_voting_weight_image=execution.output_file("[ATLASVOTINGWEIGHTIMAGEFILENAMEFORMAT]"),
    )
    return ret


def ants_joint_fusion_execute(
    params: AntsJointFusionParameters,
    execution: Execution,
) -> AntsJointFusionOutputs:
    """
    antsJointFusion is an image fusion algorithm developed by Hongzhi Wang and Paul
    Yushkevich. This implementation is based on Paul's original ITK-style
    implementation and Brian's ANTsR implementation. The original label fusion
    framework was extended to accommodate intensities.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsJointFusionOutputs`).
    """
    params = execution.params(params)
    cargs = ants_joint_fusion_cargs(params, execution)
    ret = ants_joint_fusion_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_joint_fusion(
    target_image: list[InputPathType],
    atlas_image: list[InputPathType],
    atlas_segmentation: InputPathType,
    output: str,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    alpha: float | None = 0.1,
    beta: float | None = 2.0,
    constrain_nonnegative: typing.Literal[0, 1] | None = None,
    patch_radius: str | None = "2x2x2",
    patch_metric: typing.Literal["PC", "MSQ"] | None = "PC",
    search_radius: str | None = "3x3x3",
    exclusion_image: InputPathType | None = None,
    mask_image: InputPathType | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> AntsJointFusionOutputs:
    """
    antsJointFusion is an image fusion algorithm developed by Hongzhi Wang and Paul
    Yushkevich. This implementation is based on Paul's original ITK-style
    implementation and Brian's ANTsR implementation. The original label fusion
    framework was extended to accommodate intensities.
    
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
        image_dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, the program tries to\
            infer the dimensionality from the input image.
        alpha: Regularization term added to matrix Mx for calculating the\
            inverse. Default = 0.1.
        beta: Exponent for mapping intensity difference to the joint error.\
            Default = 2.0.
        constrain_nonnegative: Constrain solution to non-negative weights.
        patch_radius: Patch radius for similarity measures. Default = 2x2x2.
        patch_metric: Metric to be used in determining the most similar\
            neighborhood patch. Options include Pearson's correlation (PC) and mean\
            squares (MSQ). Default = PC (Pearson correlation).
        search_radius: Search radius for similarity measures. Default = 3x3x3.\
            One can also specify an image where the value at the voxel specifies\
            the isotropic search radius at that voxel.
        exclusion_image: Specify an exclusion region for the given label.
        mask_image: If a mask image is specified, fusion is only performed in\
            the mask region.
        verbose: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsJointFusionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_JOINT_FUSION_METADATA)
    params = ants_joint_fusion_params(
        image_dimensionality=image_dimensionality,
        target_image=target_image,
        atlas_image=atlas_image,
        atlas_segmentation=atlas_segmentation,
        alpha=alpha,
        beta=beta,
        constrain_nonnegative=constrain_nonnegative,
        patch_radius=patch_radius,
        patch_metric=patch_metric,
        search_radius=search_radius,
        exclusion_image=exclusion_image,
        mask_image=mask_image,
        output=output,
        verbose=verbose,
    )
    return ants_joint_fusion_execute(params, execution)


__all__ = [
    "ANTS_JOINT_FUSION_METADATA",
    "AntsJointFusionOutputs",
    "AntsJointFusionParameters",
    "ants_joint_fusion",
    "ants_joint_fusion_params",
]
