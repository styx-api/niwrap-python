# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__THICKNESS_MASTER_METADATA = Metadata(
    id="16b2f3c5546e0b51fc57c90130ccb25d83ec244f.boutiques",
    name="@thickness_master",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VThicknessMasterParameters = typing.TypedDict('VThicknessMasterParameters', {
    "__STYX_TYPE__": typing.Literal["@thickness_master"],
    "maskset": InputPathType,
    "surfset": InputPathType,
    "outdir": typing.NotRequired[str | None],
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
        "@thickness_master": v__thickness_master_cargs,
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
        "@thickness_master": v__thickness_master_outputs,
    }.get(t)


class VThicknessMasterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__thickness_master(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_bb_dir: OutputPathType | None
    """Output directory for ball and box method"""
    output_erode_dir: OutputPathType | None
    """Output directory for erosion method"""
    output_in2out_dir: OutputPathType | None
    """Output directory for in2out method"""


def v__thickness_master_params(
    maskset: InputPathType,
    surfset: InputPathType,
    outdir: str | None = None,
) -> VThicknessMasterParameters:
    """
    Build parameters.
    
    Args:
        maskset: Mask dataset to find thickness.
        surfset: Surface dataset to use for normals into the volume.
        outdir: Output directory base name. The output will be placed in a\
            directory with thick_base in its name (e.g., mmmm_bb, mmmm_erode,\
            mmmm_in2out).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@thickness_master",
        "maskset": maskset,
        "surfset": surfset,
    }
    if outdir is not None:
        params["outdir"] = outdir
    return params


def v__thickness_master_cargs(
    params: VThicknessMasterParameters,
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
    cargs.append("@thickness_master")
    cargs.extend([
        "-maskset",
        execution.input_file(params.get("maskset"))
    ])
    cargs.extend([
        "-surfset",
        execution.input_file(params.get("surfset"))
    ])
    if params.get("outdir") is not None:
        cargs.extend([
            "-outdir",
            params.get("outdir")
        ])
    return cargs


def v__thickness_master_outputs(
    params: VThicknessMasterParameters,
    execution: Execution,
) -> VThicknessMasterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VThicknessMasterOutputs(
        root=execution.output_file("."),
        output_bb_dir=execution.output_file(params.get("outdir") + "_bb/") if (params.get("outdir") is not None) else None,
        output_erode_dir=execution.output_file(params.get("outdir") + "_erode/") if (params.get("outdir") is not None) else None,
        output_in2out_dir=execution.output_file(params.get("outdir") + "_in2out/") if (params.get("outdir") is not None) else None,
    )
    return ret


def v__thickness_master_execute(
    params: VThicknessMasterParameters,
    execution: Execution,
) -> VThicknessMasterOutputs:
    """
    Compute cortical thickness using mask and surface datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VThicknessMasterOutputs`).
    """
    params = execution.params(params)
    cargs = v__thickness_master_cargs(params, execution)
    ret = v__thickness_master_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__thickness_master(
    maskset: InputPathType,
    surfset: InputPathType,
    outdir: str | None = None,
    runner: Runner | None = None,
) -> VThicknessMasterOutputs:
    """
    Compute cortical thickness using mask and surface datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        maskset: Mask dataset to find thickness.
        surfset: Surface dataset to use for normals into the volume.
        outdir: Output directory base name. The output will be placed in a\
            directory with thick_base in its name (e.g., mmmm_bb, mmmm_erode,\
            mmmm_in2out).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VThicknessMasterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__THICKNESS_MASTER_METADATA)
    params = v__thickness_master_params(
        maskset=maskset,
        surfset=surfset,
        outdir=outdir,
    )
    return v__thickness_master_execute(params, execution)


__all__ = [
    "VThicknessMasterOutputs",
    "VThicknessMasterParameters",
    "V__THICKNESS_MASTER_METADATA",
    "v__thickness_master",
    "v__thickness_master_params",
]
