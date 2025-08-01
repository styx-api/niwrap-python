# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_BRAIN_VOYAGERTO_AFNI_METADATA = Metadata(
    id="5fa4482f1d05556b8c1f6948d6ca7a34ed478089.boutiques",
    name="3dBRAIN_VOYAGERtoAFNI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dBrainVoyagertoAfniParameters = typing.TypedDict('V3dBrainVoyagertoAfniParameters', {
    "__STYXTYPE__": typing.Literal["3dBRAIN_VOYAGERtoAFNI"],
    "input_file": InputPathType,
    "force_byte_swap": bool,
    "brainvoyager_qx": bool,
    "tlrc_space": bool,
    "acpc_space": bool,
    "orig_space": bool,
    "prefix": typing.NotRequired[str | None],
    "novolreg": bool,
    "noxform": bool,
    "set_environment": typing.NotRequired[str | None],
    "trace_debugging": bool,
    "trace_extreme_debugging": bool,
    "turn_off_memory_tracing": bool,
    "turn_on_memory_tracing": bool,
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
        "3dBRAIN_VOYAGERtoAFNI": v_3d_brain_voyagerto_afni_cargs,
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
        "3dBRAIN_VOYAGERtoAFNI": v_3d_brain_voyagerto_afni_outputs,
    }.get(t)


class V3dBrainVoyagertoAfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_brain_voyagerto_afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik_file: OutputPathType
    """Output BRIK file"""
    output_head_file: OutputPathType
    """Output HEAD file"""


def v_3d_brain_voyagerto_afni_params(
    input_file: InputPathType,
    force_byte_swap: bool = False,
    brainvoyager_qx: bool = False,
    tlrc_space: bool = False,
    acpc_space: bool = False,
    orig_space: bool = False,
    prefix: str | None = None,
    novolreg: bool = False,
    noxform: bool = False,
    set_environment: str | None = None,
    trace_debugging: bool = False,
    trace_extreme_debugging: bool = False,
    turn_off_memory_tracing: bool = False,
    turn_on_memory_tracing: bool = False,
) -> V3dBrainVoyagertoAfniParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input BrainVoyager VMR file.
        force_byte_swap: Force byte swapping.
        brainvoyager_qx: .vmr file is from BrainVoyager QX.
        tlrc_space: Dset in tlrc space.
        acpc_space: Dset in acpc-aligned space.
        orig_space: Dset in orig space.
        prefix: Prefix for output files.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        noxform: Same as -novolreg.
        set_environment: Set environment variable ENVname to be ENVvalue.\
            Quotes are necessary.
        trace_debugging: Turns on In/Out debug and Memory tracing.
        trace_extreme_debugging: Turns on extreme tracing.
        turn_off_memory_tracing: Turn off memory tracing.
        turn_on_memory_tracing: Turn on memory tracing (default).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dBRAIN_VOYAGERtoAFNI",
        "input_file": input_file,
        "force_byte_swap": force_byte_swap,
        "brainvoyager_qx": brainvoyager_qx,
        "tlrc_space": tlrc_space,
        "acpc_space": acpc_space,
        "orig_space": orig_space,
        "novolreg": novolreg,
        "noxform": noxform,
        "trace_debugging": trace_debugging,
        "trace_extreme_debugging": trace_extreme_debugging,
        "turn_off_memory_tracing": turn_off_memory_tracing,
        "turn_on_memory_tracing": turn_on_memory_tracing,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if set_environment is not None:
        params["set_environment"] = set_environment
    return params


def v_3d_brain_voyagerto_afni_cargs(
    params: V3dBrainVoyagertoAfniParameters,
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
    cargs.append("3dBRAIN_VOYAGERtoAFNI")
    cargs.extend([
        "--input",
        execution.input_file(params.get("input_file"))
    ])
    if params.get("force_byte_swap"):
        cargs.append("-bs")
    if params.get("brainvoyager_qx"):
        cargs.append("-qx")
    if params.get("tlrc_space"):
        cargs.append("-tlrc")
    if params.get("acpc_space"):
        cargs.append("-acpc")
    if params.get("orig_space"):
        cargs.append("-orig")
    if params.get("prefix") is not None:
        cargs.extend([
            "--prefix",
            params.get("prefix")
        ])
    if params.get("novolreg"):
        cargs.append("-novolreg")
    if params.get("noxform"):
        cargs.append("-noxform")
    if params.get("set_environment") is not None:
        cargs.extend([
            "-setenv",
            params.get("set_environment")
        ])
    if params.get("trace_debugging"):
        cargs.append("-trace")
    if params.get("trace_extreme_debugging"):
        cargs.append("-TRACE")
    if params.get("turn_off_memory_tracing"):
        cargs.append("-nomall")
    if params.get("turn_on_memory_tracing"):
        cargs.append("-yesmall")
    return cargs


def v_3d_brain_voyagerto_afni_outputs(
    params: V3dBrainVoyagertoAfniParameters,
    execution: Execution,
) -> V3dBrainVoyagertoAfniOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dBrainVoyagertoAfniOutputs(
        root=execution.output_file("."),
        output_brik_file=execution.output_file("output.BRIK"),
        output_head_file=execution.output_file("output.HEAD"),
    )
    return ret


def v_3d_brain_voyagerto_afni_execute(
    params: V3dBrainVoyagertoAfniParameters,
    execution: Execution,
) -> V3dBrainVoyagertoAfniOutputs:
    """
    Converts a BrainVoyager vmr dataset to AFNI's BRIK format based on information
    from BrainVoyager's website.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dBrainVoyagertoAfniOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_brain_voyagerto_afni_cargs(params, execution)
    ret = v_3d_brain_voyagerto_afni_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_brain_voyagerto_afni(
    input_file: InputPathType,
    force_byte_swap: bool = False,
    brainvoyager_qx: bool = False,
    tlrc_space: bool = False,
    acpc_space: bool = False,
    orig_space: bool = False,
    prefix: str | None = None,
    novolreg: bool = False,
    noxform: bool = False,
    set_environment: str | None = None,
    trace_debugging: bool = False,
    trace_extreme_debugging: bool = False,
    turn_off_memory_tracing: bool = False,
    turn_on_memory_tracing: bool = False,
    runner: Runner | None = None,
) -> V3dBrainVoyagertoAfniOutputs:
    """
    Converts a BrainVoyager vmr dataset to AFNI's BRIK format based on information
    from BrainVoyager's website.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input BrainVoyager VMR file.
        force_byte_swap: Force byte swapping.
        brainvoyager_qx: .vmr file is from BrainVoyager QX.
        tlrc_space: Dset in tlrc space.
        acpc_space: Dset in acpc-aligned space.
        orig_space: Dset in orig space.
        prefix: Prefix for output files.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        noxform: Same as -novolreg.
        set_environment: Set environment variable ENVname to be ENVvalue.\
            Quotes are necessary.
        trace_debugging: Turns on In/Out debug and Memory tracing.
        trace_extreme_debugging: Turns on extreme tracing.
        turn_off_memory_tracing: Turn off memory tracing.
        turn_on_memory_tracing: Turn on memory tracing (default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBrainVoyagertoAfniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BRAIN_VOYAGERTO_AFNI_METADATA)
    params = v_3d_brain_voyagerto_afni_params(
        input_file=input_file,
        force_byte_swap=force_byte_swap,
        brainvoyager_qx=brainvoyager_qx,
        tlrc_space=tlrc_space,
        acpc_space=acpc_space,
        orig_space=orig_space,
        prefix=prefix,
        novolreg=novolreg,
        noxform=noxform,
        set_environment=set_environment,
        trace_debugging=trace_debugging,
        trace_extreme_debugging=trace_extreme_debugging,
        turn_off_memory_tracing=turn_off_memory_tracing,
        turn_on_memory_tracing=turn_on_memory_tracing,
    )
    return v_3d_brain_voyagerto_afni_execute(params, execution)


__all__ = [
    "V3dBrainVoyagertoAfniOutputs",
    "V3dBrainVoyagertoAfniParameters",
    "V_3D_BRAIN_VOYAGERTO_AFNI_METADATA",
    "v_3d_brain_voyagerto_afni",
    "v_3d_brain_voyagerto_afni_params",
]
