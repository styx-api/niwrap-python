# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_MATCH_METADATA = Metadata(
    id="5a9b48cc507b88f6620f1b745b682a96b9bb92f5.boutiques",
    name="3dMatch",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dMatchParameters = typing.TypedDict('V3dMatchParameters', {
    "__STYX_TYPE__": typing.Literal["3dMatch"],
    "inset": InputPathType,
    "refset": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "in_min": typing.NotRequired[float | None],
    "in_max": typing.NotRequired[float | None],
    "ref_min": typing.NotRequired[float | None],
    "ref_max": typing.NotRequired[float | None],
    "prefix": str,
    "only_dice_thr": bool,
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
        "3dMatch": v_3d_match_cargs,
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
        "3dMatch": v_3d_match_outputs,
    }.get(t)


class V3dMatchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_match(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    ref_brik: OutputPathType
    """AFNI BRIK file with the same number of subbricks as the refset file, with
    highest weighted correlation."""
    ref_coeff_vals: OutputPathType
    """Text file recording original indices and coefficients."""
    in_brik: OutputPathType
    """AFNI BRIK file with the same number of subbricks as the inset file, with
    highest weighted correlation."""
    in_coeff_vals: OutputPathType
    """Text file recording original indices and coefficients."""


def v_3d_match_params(
    inset: InputPathType,
    refset: InputPathType,
    prefix: str,
    mask: InputPathType | None = None,
    in_min: float | None = None,
    in_max: float | None = None,
    ref_min: float | None = None,
    ref_max: float | None = None,
    only_dice_thr: bool = False,
) -> V3dMatchParameters:
    """
    Build parameters.
    
    Args:
        inset: File with M subbricks of data to match against another file.
        refset: File with N subbricks, serving as a reference for INPUT_FILE.
        prefix: Prefix for output name for BRIK/HEAD files and *_coeff.vals\
            text files.
        mask: A mask of regions to include in the correlation of datasets.
        in_min: Threshold below which values in INPUT_FILE will be zeroed\
            during analysis.
        in_max: Threshold above which values in INPUT_FILE will be zeroed\
            during analysis.
        ref_min: Threshold below which values in REF_FILE will be zeroed during\
            analysis.
        ref_max: Threshold above which values in REF_FILE will be zeroed during\
            analysis.
        only_dice_thr: Apply thresholding only during Dice evaluation, not\
            during spatial correlation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dMatch",
        "inset": inset,
        "refset": refset,
        "prefix": prefix,
        "only_dice_thr": only_dice_thr,
    }
    if mask is not None:
        params["mask"] = mask
    if in_min is not None:
        params["in_min"] = in_min
    if in_max is not None:
        params["in_max"] = in_max
    if ref_min is not None:
        params["ref_min"] = ref_min
    if ref_max is not None:
        params["ref_max"] = ref_max
    return params


def v_3d_match_cargs(
    params: V3dMatchParameters,
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
    cargs.append("3dMatch")
    cargs.extend([
        "-inset",
        execution.input_file(params.get("inset"))
    ])
    cargs.extend([
        "-refset",
        execution.input_file(params.get("refset"))
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("in_min") is not None:
        cargs.extend([
            "-in_min",
            str(params.get("in_min"))
        ])
    if params.get("in_max") is not None:
        cargs.extend([
            "-in_max",
            str(params.get("in_max"))
        ])
    if params.get("ref_min") is not None:
        cargs.extend([
            "-ref_min",
            str(params.get("ref_min"))
        ])
    if params.get("ref_max") is not None:
        cargs.extend([
            "-ref_max",
            str(params.get("ref_max"))
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("only_dice_thr"):
        cargs.append("-only_dice_thr")
    return cargs


def v_3d_match_outputs(
    params: V3dMatchParameters,
    execution: Execution,
) -> V3dMatchOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dMatchOutputs(
        root=execution.output_file("."),
        ref_brik=execution.output_file(params.get("prefix") + "_REF+orig.BRIK"),
        ref_coeff_vals=execution.output_file(params.get("prefix") + "_REF_coeff.vals"),
        in_brik=execution.output_file(params.get("prefix") + "_IN+orig.BRIK"),
        in_coeff_vals=execution.output_file(params.get("prefix") + "_IN_coeff.vals"),
    )
    return ret


def v_3d_match_execute(
    params: V3dMatchParameters,
    execution: Execution,
) -> V3dMatchOutputs:
    """
    Find similar subbricks and rearrange order to ease comparison. Part of FATCAT in
    AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dMatchOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_match_cargs(params, execution)
    ret = v_3d_match_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_match(
    inset: InputPathType,
    refset: InputPathType,
    prefix: str,
    mask: InputPathType | None = None,
    in_min: float | None = None,
    in_max: float | None = None,
    ref_min: float | None = None,
    ref_max: float | None = None,
    only_dice_thr: bool = False,
    runner: Runner | None = None,
) -> V3dMatchOutputs:
    """
    Find similar subbricks and rearrange order to ease comparison. Part of FATCAT in
    AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        inset: File with M subbricks of data to match against another file.
        refset: File with N subbricks, serving as a reference for INPUT_FILE.
        prefix: Prefix for output name for BRIK/HEAD files and *_coeff.vals\
            text files.
        mask: A mask of regions to include in the correlation of datasets.
        in_min: Threshold below which values in INPUT_FILE will be zeroed\
            during analysis.
        in_max: Threshold above which values in INPUT_FILE will be zeroed\
            during analysis.
        ref_min: Threshold below which values in REF_FILE will be zeroed during\
            analysis.
        ref_max: Threshold above which values in REF_FILE will be zeroed during\
            analysis.
        only_dice_thr: Apply thresholding only during Dice evaluation, not\
            during spatial correlation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMatchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MATCH_METADATA)
    params = v_3d_match_params(
        inset=inset,
        refset=refset,
        mask=mask,
        in_min=in_min,
        in_max=in_max,
        ref_min=ref_min,
        ref_max=ref_max,
        prefix=prefix,
        only_dice_thr=only_dice_thr,
    )
    return v_3d_match_execute(params, execution)


__all__ = [
    "V3dMatchOutputs",
    "V3dMatchParameters",
    "V_3D_MATCH_METADATA",
    "v_3d_match",
    "v_3d_match_params",
]
