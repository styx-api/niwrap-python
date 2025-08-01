# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_SPAT_NORM_METADATA = Metadata(
    id="5e25808dc97cedae2e2d6f6da2b00952c1719962.boutiques",
    name="3dSpatNorm",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dSpatNormParameters = typing.TypedDict('V3dSpatNormParameters', {
    "__STYXTYPE__": typing.Literal["3dSpatNorm"],
    "dataset": InputPathType,
    "prefix": typing.NotRequired[str | None],
    "orig_space": bool,
    "verbose": bool,
    "monkey": bool,
    "marmot": bool,
    "rat": bool,
    "human": bool,
    "bottom_cuts": typing.NotRequired[str | None],
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
        "3dSpatNorm": v_3d_spat_norm_cargs,
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
        "3dSpatNorm": v_3d_spat_norm_outputs,
    }.get(t)


class V3dSpatNormOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_spat_norm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_head: OutputPathType | None
    """Output dataset (HEAD file)"""
    out_brik: OutputPathType | None
    """Output dataset (BRIK file)"""


def v_3d_spat_norm_params(
    dataset: InputPathType,
    prefix: str | None = None,
    orig_space: bool = False,
    verbose: bool = False,
    monkey: bool = False,
    marmot: bool = False,
    rat: bool = False,
    human: bool = False,
    bottom_cuts: str | None = None,
) -> V3dSpatNormParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input dataset.
        prefix: Write output dataset using 'ppp' for the prefix.
        orig_space: Write output dataset using the same grid as dataset.
        verbose: Write out progress reports.
        monkey: Monkey business.
        marmot: Marmoset head.
        rat: Rat head.
        human: Bone head (default).
        bottom_cuts: Make approximate cuts at the bottom to shave non-brain\
            areas. CUTFLAGS is a string of characters indicating which sides to\
            cut: 'A' for anterior, 'P' for posterior, 'R' for right, 'L' for left.\
            Example: -bottom_cuts APLR.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dSpatNorm",
        "dataset": dataset,
        "orig_space": orig_space,
        "verbose": verbose,
        "monkey": monkey,
        "marmot": marmot,
        "rat": rat,
        "human": human,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if bottom_cuts is not None:
        params["bottom_cuts"] = bottom_cuts
    return params


def v_3d_spat_norm_cargs(
    params: V3dSpatNormParameters,
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
    cargs.append("3dSpatNorm")
    cargs.append(execution.input_file(params.get("dataset")))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("orig_space"):
        cargs.append("-orig_space")
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("monkey"):
        cargs.append("-monkey")
    if params.get("marmot"):
        cargs.append("-marmost")
    if params.get("rat"):
        cargs.append("-rat")
    if params.get("human"):
        cargs.append("-human")
    if params.get("bottom_cuts") is not None:
        cargs.extend([
            "-bottom_cuts",
            params.get("bottom_cuts")
        ])
    return cargs


def v_3d_spat_norm_outputs(
    params: V3dSpatNormParameters,
    execution: Execution,
) -> V3dSpatNormOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dSpatNormOutputs(
        root=execution.output_file("."),
        out_head=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
        out_brik=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_spat_norm_execute(
    params: V3dSpatNormParameters,
    execution: Execution,
) -> V3dSpatNormOutputs:
    """
    An obsolete tool for spatial normalization.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dSpatNormOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_spat_norm_cargs(params, execution)
    ret = v_3d_spat_norm_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_spat_norm(
    dataset: InputPathType,
    prefix: str | None = None,
    orig_space: bool = False,
    verbose: bool = False,
    monkey: bool = False,
    marmot: bool = False,
    rat: bool = False,
    human: bool = False,
    bottom_cuts: str | None = None,
    runner: Runner | None = None,
) -> V3dSpatNormOutputs:
    """
    An obsolete tool for spatial normalization.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset.
        prefix: Write output dataset using 'ppp' for the prefix.
        orig_space: Write output dataset using the same grid as dataset.
        verbose: Write out progress reports.
        monkey: Monkey business.
        marmot: Marmoset head.
        rat: Rat head.
        human: Bone head (default).
        bottom_cuts: Make approximate cuts at the bottom to shave non-brain\
            areas. CUTFLAGS is a string of characters indicating which sides to\
            cut: 'A' for anterior, 'P' for posterior, 'R' for right, 'L' for left.\
            Example: -bottom_cuts APLR.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSpatNormOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SPAT_NORM_METADATA)
    params = v_3d_spat_norm_params(
        dataset=dataset,
        prefix=prefix,
        orig_space=orig_space,
        verbose=verbose,
        monkey=monkey,
        marmot=marmot,
        rat=rat,
        human=human,
        bottom_cuts=bottom_cuts,
    )
    return v_3d_spat_norm_execute(params, execution)


__all__ = [
    "V3dSpatNormOutputs",
    "V3dSpatNormParameters",
    "V_3D_SPAT_NORM_METADATA",
    "v_3d_spat_norm",
    "v_3d_spat_norm_params",
]
