# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__EXAMINE_GEN_FEAT_DISTS_METADATA = Metadata(
    id="60ac2c94312fce85a0d90163607df55149e2869d.boutiques",
    name="@ExamineGenFeatDists",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VExamineGenFeatDistsParameters = typing.TypedDict('VExamineGenFeatDistsParameters', {
    "__STYX_TYPE__": typing.Literal["@ExamineGenFeatDists"],
    "features_dir": str,
    "wildcards": typing.NotRequired[list[str] | None],
    "output_suffix": typing.NotRequired[str | None],
    "exclude_features": typing.NotRequired[list[str] | None],
    "exclude_classes": typing.NotRequired[list[str] | None],
    "output_dir": typing.NotRequired[str | None],
    "panels_horizontal": typing.NotRequired[float | None],
    "echo": bool,
    "help": bool,
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
        "@ExamineGenFeatDists": v__examine_gen_feat_dists_cargs,
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
    }.get(t)


class VExamineGenFeatDistsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__examine_gen_feat_dists(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__examine_gen_feat_dists_params(
    features_dir: str,
    wildcards: list[str] | None = None,
    output_suffix: str | None = None,
    exclude_features: list[str] | None = None,
    exclude_classes: list[str] | None = None,
    output_dir: str | None = None,
    panels_horizontal: float | None = None,
    echo: bool = False,
    help_: bool = False,
) -> VExamineGenFeatDistsParameters:
    """
    Build parameters.
    
    Args:
        features_dir: Output directory of 3dGenFeatDists.
        wildcards: Wildcards used to select feature histograms under the\
            directory.
        output_suffix: Output suffix, added to output images. Default is\
            'nosuff'.
        exclude_features: Exclude following features. String matching is\
            partial.
        exclude_classes: Exclude following classes. String matching is partial.
        output_dir: Output directory, default is the same as -fdir.
        panels_horizontal: Set number of panels along the horizontal direction.
        echo: Set echo.
        help_: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ExamineGenFeatDists",
        "features_dir": features_dir,
        "echo": echo,
        "help": help_,
    }
    if wildcards is not None:
        params["wildcards"] = wildcards
    if output_suffix is not None:
        params["output_suffix"] = output_suffix
    if exclude_features is not None:
        params["exclude_features"] = exclude_features
    if exclude_classes is not None:
        params["exclude_classes"] = exclude_classes
    if output_dir is not None:
        params["output_dir"] = output_dir
    if panels_horizontal is not None:
        params["panels_horizontal"] = panels_horizontal
    return params


def v__examine_gen_feat_dists_cargs(
    params: VExamineGenFeatDistsParameters,
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
    cargs.append("@ExamineGenFeatDists")
    cargs.extend([
        "-fdir",
        params.get("features_dir")
    ])
    if params.get("wildcards") is not None:
        cargs.extend([
            "-fwild",
            *params.get("wildcards")
        ])
    if params.get("output_suffix") is not None:
        cargs.extend([
            "-suffix",
            params.get("output_suffix")
        ])
    if params.get("exclude_features") is not None:
        cargs.extend([
            "-exfeat",
            *params.get("exclude_features")
        ])
    if params.get("exclude_classes") is not None:
        cargs.extend([
            "-exclass",
            *params.get("exclude_classes")
        ])
    if params.get("output_dir") is not None:
        cargs.extend([
            "-odir",
            params.get("output_dir")
        ])
    if params.get("panels_horizontal") is not None:
        cargs.extend([
            "-nx",
            str(params.get("panels_horizontal"))
        ])
    if params.get("echo"):
        cargs.append("-echo")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def v__examine_gen_feat_dists_outputs(
    params: VExamineGenFeatDistsParameters,
    execution: Execution,
) -> VExamineGenFeatDistsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VExamineGenFeatDistsOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__examine_gen_feat_dists_execute(
    params: VExamineGenFeatDistsParameters,
    execution: Execution,
) -> VExamineGenFeatDistsOutputs:
    """
    Examine histograms produced by 3dGenFeatDists.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VExamineGenFeatDistsOutputs`).
    """
    params = execution.params(params)
    cargs = v__examine_gen_feat_dists_cargs(params, execution)
    ret = v__examine_gen_feat_dists_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__examine_gen_feat_dists(
    features_dir: str,
    wildcards: list[str] | None = None,
    output_suffix: str | None = None,
    exclude_features: list[str] | None = None,
    exclude_classes: list[str] | None = None,
    output_dir: str | None = None,
    panels_horizontal: float | None = None,
    echo: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> VExamineGenFeatDistsOutputs:
    """
    Examine histograms produced by 3dGenFeatDists.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        features_dir: Output directory of 3dGenFeatDists.
        wildcards: Wildcards used to select feature histograms under the\
            directory.
        output_suffix: Output suffix, added to output images. Default is\
            'nosuff'.
        exclude_features: Exclude following features. String matching is\
            partial.
        exclude_classes: Exclude following classes. String matching is partial.
        output_dir: Output directory, default is the same as -fdir.
        panels_horizontal: Set number of panels along the horizontal direction.
        echo: Set echo.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VExamineGenFeatDistsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__EXAMINE_GEN_FEAT_DISTS_METADATA)
    params = v__examine_gen_feat_dists_params(
        features_dir=features_dir,
        wildcards=wildcards,
        output_suffix=output_suffix,
        exclude_features=exclude_features,
        exclude_classes=exclude_classes,
        output_dir=output_dir,
        panels_horizontal=panels_horizontal,
        echo=echo,
        help_=help_,
    )
    return v__examine_gen_feat_dists_execute(params, execution)


__all__ = [
    "VExamineGenFeatDistsOutputs",
    "VExamineGenFeatDistsParameters",
    "V__EXAMINE_GEN_FEAT_DISTS_METADATA",
    "v__examine_gen_feat_dists",
    "v__examine_gen_feat_dists_params",
]
