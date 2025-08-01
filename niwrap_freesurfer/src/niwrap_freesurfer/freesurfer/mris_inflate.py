# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_INFLATE_METADATA = Metadata(
    id="8413bd9727e7211f290ec92777a3dd6eb3902178.boutiques",
    name="mris_inflate",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisInflateParameters = typing.TypedDict('MrisInflateParameters', {
    "__STYXTYPE__": typing.Literal["mris_inflate"],
    "input_surface": InputPathType,
    "output_surface": str,
    "max_iterations": typing.NotRequired[float | None],
    "snapshot_interval": typing.NotRequired[float | None],
    "dist_coefficient": typing.NotRequired[float | None],
    "no_save_sulc": bool,
    "sulcname": typing.NotRequired[str | None],
    "mm_flag": bool,
    "scale_flag": typing.NotRequired[float | None],
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
        "mris_inflate": mris_inflate_cargs,
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
        "mris_inflate": mris_inflate_outputs,
    }.get(t)


class MrisInflateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_inflate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_file: OutputPathType
    """Output surface file"""


def mris_inflate_params(
    input_surface: InputPathType,
    output_surface: str,
    max_iterations: float | None = None,
    snapshot_interval: float | None = None,
    dist_coefficient: float | None = None,
    no_save_sulc: bool = False,
    sulcname: str | None = None,
    mm_flag: bool = False,
    scale_flag: float | None = None,
) -> MrisInflateParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file.
        output_surface: Output surface file.
        max_iterations: Set the maximum number of iterations (default: 10).
        snapshot_interval: Write out a snapshot of the inflation every\
            specified time step.
        dist_coefficient: Specify the relative strength of the metric\
            preserving term in the cost functional versus the smoothing term\
            (default: 0.1).
        no_save_sulc: Do not save ?h.sulc.
        sulcname: Save to ?h.sulcname.
        mm_flag: Compute sulc in mm without zero meaning or scaling.
        scale_flag: Disable or enable scaling of inflated brain.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_inflate",
        "input_surface": input_surface,
        "output_surface": output_surface,
        "no_save_sulc": no_save_sulc,
        "mm_flag": mm_flag,
    }
    if max_iterations is not None:
        params["max_iterations"] = max_iterations
    if snapshot_interval is not None:
        params["snapshot_interval"] = snapshot_interval
    if dist_coefficient is not None:
        params["dist_coefficient"] = dist_coefficient
    if sulcname is not None:
        params["sulcname"] = sulcname
    if scale_flag is not None:
        params["scale_flag"] = scale_flag
    return params


def mris_inflate_cargs(
    params: MrisInflateParameters,
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
    cargs.append("mris_inflate")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(params.get("output_surface"))
    if params.get("max_iterations") is not None:
        cargs.extend([
            "-n",
            str(params.get("max_iterations"))
        ])
    if params.get("snapshot_interval") is not None:
        cargs.extend([
            "-w",
            str(params.get("snapshot_interval"))
        ])
    if params.get("dist_coefficient") is not None:
        cargs.extend([
            "-dist",
            str(params.get("dist_coefficient"))
        ])
    if params.get("no_save_sulc"):
        cargs.append("-no-save-sulc")
    if params.get("sulcname") is not None:
        cargs.extend([
            "-sulc",
            params.get("sulcname")
        ])
    if params.get("mm_flag"):
        cargs.append("-mm")
    if params.get("scale_flag") is not None:
        cargs.extend([
            "-scale",
            str(params.get("scale_flag"))
        ])
    return cargs


def mris_inflate_outputs(
    params: MrisInflateParameters,
    execution: Execution,
) -> MrisInflateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisInflateOutputs(
        root=execution.output_file("."),
        output_surface_file=execution.output_file(params.get("output_surface")),
    )
    return ret


def mris_inflate_execute(
    params: MrisInflateParameters,
    execution: Execution,
) -> MrisInflateOutputs:
    """
    Cortical surface inflation tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisInflateOutputs`).
    """
    params = execution.params(params)
    cargs = mris_inflate_cargs(params, execution)
    ret = mris_inflate_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_inflate(
    input_surface: InputPathType,
    output_surface: str,
    max_iterations: float | None = None,
    snapshot_interval: float | None = None,
    dist_coefficient: float | None = None,
    no_save_sulc: bool = False,
    sulcname: str | None = None,
    mm_flag: bool = False,
    scale_flag: float | None = None,
    runner: Runner | None = None,
) -> MrisInflateOutputs:
    """
    Cortical surface inflation tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        output_surface: Output surface file.
        max_iterations: Set the maximum number of iterations (default: 10).
        snapshot_interval: Write out a snapshot of the inflation every\
            specified time step.
        dist_coefficient: Specify the relative strength of the metric\
            preserving term in the cost functional versus the smoothing term\
            (default: 0.1).
        no_save_sulc: Do not save ?h.sulc.
        sulcname: Save to ?h.sulcname.
        mm_flag: Compute sulc in mm without zero meaning or scaling.
        scale_flag: Disable or enable scaling of inflated brain.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisInflateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_INFLATE_METADATA)
    params = mris_inflate_params(
        input_surface=input_surface,
        output_surface=output_surface,
        max_iterations=max_iterations,
        snapshot_interval=snapshot_interval,
        dist_coefficient=dist_coefficient,
        no_save_sulc=no_save_sulc,
        sulcname=sulcname,
        mm_flag=mm_flag,
        scale_flag=scale_flag,
    )
    return mris_inflate_execute(params, execution)


__all__ = [
    "MRIS_INFLATE_METADATA",
    "MrisInflateOutputs",
    "MrisInflateParameters",
    "mris_inflate",
    "mris_inflate_params",
]
