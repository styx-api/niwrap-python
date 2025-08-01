# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_THICKNESS_DIFF_METADATA = Metadata(
    id="95efc622125bf8bcd42b0208effbdbe434d5b062.boutiques",
    name="mris_thickness_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisThicknessDiffParameters = typing.TypedDict('MrisThicknessDiffParameters', {
    "__STYXTYPE__": typing.Literal["mris_thickness_diff"],
    "src_type": typing.NotRequired[str | None],
    "trg_type": typing.NotRequired[str | None],
    "out_file": str,
    "out_resampled": typing.NotRequired[str | None],
    "nsmooth": typing.NotRequired[float | None],
    "register": bool,
    "xform": typing.NotRequired[InputPathType | None],
    "invert": bool,
    "src_volume": typing.NotRequired[InputPathType | None],
    "dst_volume": typing.NotRequired[InputPathType | None],
    "abs": bool,
    "log_file": typing.NotRequired[InputPathType | None],
    "subject_name": typing.NotRequired[str | None],
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
        "mris_thickness_diff": mris_thickness_diff_cargs,
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
        "mris_thickness_diff": mris_thickness_diff_outputs,
    }.get(t)


class MrisThicknessDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_thickness_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_difference: OutputPathType
    """Output file with the difference mapped onto the surface"""
    output_resampled: OutputPathType | None
    """Resampled output thickness file"""


def mris_thickness_diff_params(
    out_file: str,
    src_type: str | None = None,
    trg_type: str | None = None,
    out_resampled: str | None = None,
    nsmooth: float | None = None,
    register: bool = False,
    xform: InputPathType | None = None,
    invert: bool = False,
    src_volume: InputPathType | None = None,
    dst_volume: InputPathType | None = None,
    abs_: bool = False,
    log_file: InputPathType | None = None,
    subject_name: str | None = None,
) -> MrisThicknessDiffParameters:
    """
    Build parameters.
    
    Args:
        out_file: Output file name.
        src_type: Input surface data format (curv, paint or w).
        trg_type: Output format (paint or w).
        out_resampled: Output resampled thickness.
        nsmooth: Number of smoothing steps.
        register: Perform ICP rigid registration.
        xform: Apply LTA transform to align input surface1 to surface2.
        invert: Reversely apply -xform.
        src_volume: Source volume for -xform.
        dst_volume: Target volume for -xform.
        abs_: Compute the std of abs-thickness-diff.
        log_file: Log file name.
        subject_name: Subject name (to be recorded in logfile).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_thickness_diff",
        "out_file": out_file,
        "register": register,
        "invert": invert,
        "abs": abs_,
    }
    if src_type is not None:
        params["src_type"] = src_type
    if trg_type is not None:
        params["trg_type"] = trg_type
    if out_resampled is not None:
        params["out_resampled"] = out_resampled
    if nsmooth is not None:
        params["nsmooth"] = nsmooth
    if xform is not None:
        params["xform"] = xform
    if src_volume is not None:
        params["src_volume"] = src_volume
    if dst_volume is not None:
        params["dst_volume"] = dst_volume
    if log_file is not None:
        params["log_file"] = log_file
    if subject_name is not None:
        params["subject_name"] = subject_name
    return params


def mris_thickness_diff_cargs(
    params: MrisThicknessDiffParameters,
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
    cargs.append("mris_thickness_diff")
    if params.get("src_type") is not None:
        cargs.extend([
            "-src_type",
            params.get("src_type")
        ])
    if params.get("trg_type") is not None:
        cargs.extend([
            "-trg_type",
            params.get("trg_type")
        ])
    cargs.extend([
        "-out",
        params.get("out_file")
    ])
    if params.get("out_resampled") is not None:
        cargs.extend([
            "-out_resampled",
            params.get("out_resampled")
        ])
    if params.get("nsmooth") is not None:
        cargs.extend([
            "-nsmooth",
            str(params.get("nsmooth"))
        ])
    if params.get("register"):
        cargs.append("-register")
    if params.get("xform") is not None:
        cargs.extend([
            "-xform",
            execution.input_file(params.get("xform"))
        ])
    if params.get("invert"):
        cargs.append("-invert")
    if params.get("src_volume") is not None:
        cargs.extend([
            "-src",
            execution.input_file(params.get("src_volume"))
        ])
    if params.get("dst_volume") is not None:
        cargs.extend([
            "-dst",
            execution.input_file(params.get("dst_volume"))
        ])
    if params.get("abs"):
        cargs.append("-abs")
    if params.get("log_file") is not None:
        cargs.extend([
            "-L",
            execution.input_file(params.get("log_file"))
        ])
    if params.get("subject_name") is not None:
        cargs.extend([
            "-S",
            params.get("subject_name")
        ])
    return cargs


def mris_thickness_diff_outputs(
    params: MrisThicknessDiffParameters,
    execution: Execution,
) -> MrisThicknessDiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisThicknessDiffOutputs(
        root=execution.output_file("."),
        output_difference=execution.output_file(params.get("out_file")),
        output_resampled=execution.output_file(params.get("out_resampled")) if (params.get("out_resampled") is not None) else None,
    )
    return ret


def mris_thickness_diff_execute(
    params: MrisThicknessDiffParameters,
    execution: Execution,
) -> MrisThicknessDiffOutputs:
    """
    Computes the difference of two surface data sets defined on two surface meshes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisThicknessDiffOutputs`).
    """
    params = execution.params(params)
    cargs = mris_thickness_diff_cargs(params, execution)
    ret = mris_thickness_diff_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_thickness_diff(
    out_file: str,
    src_type: str | None = None,
    trg_type: str | None = None,
    out_resampled: str | None = None,
    nsmooth: float | None = None,
    register: bool = False,
    xform: InputPathType | None = None,
    invert: bool = False,
    src_volume: InputPathType | None = None,
    dst_volume: InputPathType | None = None,
    abs_: bool = False,
    log_file: InputPathType | None = None,
    subject_name: str | None = None,
    runner: Runner | None = None,
) -> MrisThicknessDiffOutputs:
    """
    Computes the difference of two surface data sets defined on two surface meshes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        out_file: Output file name.
        src_type: Input surface data format (curv, paint or w).
        trg_type: Output format (paint or w).
        out_resampled: Output resampled thickness.
        nsmooth: Number of smoothing steps.
        register: Perform ICP rigid registration.
        xform: Apply LTA transform to align input surface1 to surface2.
        invert: Reversely apply -xform.
        src_volume: Source volume for -xform.
        dst_volume: Target volume for -xform.
        abs_: Compute the std of abs-thickness-diff.
        log_file: Log file name.
        subject_name: Subject name (to be recorded in logfile).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisThicknessDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_THICKNESS_DIFF_METADATA)
    params = mris_thickness_diff_params(
        src_type=src_type,
        trg_type=trg_type,
        out_file=out_file,
        out_resampled=out_resampled,
        nsmooth=nsmooth,
        register=register,
        xform=xform,
        invert=invert,
        src_volume=src_volume,
        dst_volume=dst_volume,
        abs_=abs_,
        log_file=log_file,
        subject_name=subject_name,
    )
    return mris_thickness_diff_execute(params, execution)


__all__ = [
    "MRIS_THICKNESS_DIFF_METADATA",
    "MrisThicknessDiffOutputs",
    "MrisThicknessDiffParameters",
    "mris_thickness_diff",
    "mris_thickness_diff_params",
]
