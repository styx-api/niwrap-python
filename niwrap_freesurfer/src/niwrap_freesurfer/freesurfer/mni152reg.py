# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MNI152REG_METADATA = Metadata(
    id="dfc37620e722a922c216aae5f87bf785a7f52f00.boutiques",
    name="mni152reg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Mni152regParameters = typing.TypedDict('Mni152regParameters', {
    "__STYXTYPE__": typing.Literal["mni152reg"],
    "subject": str,
    "register_1mm": bool,
    "output": typing.NotRequired[str | None],
    "symmetric": bool,
    "save_volume": bool,
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
        "mni152reg": mni152reg_cargs,
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
        "mni152reg": mni152reg_outputs,
    }.get(t)


class Mni152regOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mni152reg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reg_matrix_2mm: OutputPathType
    """Output registration matrix for standard 2mm target"""
    reg_matrix_1mm: OutputPathType
    """Output registration matrix for 1mm target when --1 flag is used"""


def mni152reg_params(
    subject: str,
    register_1mm: bool = False,
    output: str | None = None,
    symmetric: bool = False,
    save_volume: bool = False,
) -> Mni152regParameters:
    """
    Build parameters.
    
    Args:
        subject: FreeSurfer subject ID.
        register_1mm: Register to 1mm target (instead of 2mm).
        output: Explicitly set output registration file.
        symmetric: Register to FSL symmetric target.
        save_volume: Sample original to output space.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mni152reg",
        "subject": subject,
        "register_1mm": register_1mm,
        "symmetric": symmetric,
        "save_volume": save_volume,
    }
    if output is not None:
        params["output"] = output
    return params


def mni152reg_cargs(
    params: Mni152regParameters,
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
    cargs.append("mni152reg")
    cargs.extend([
        "-s",
        params.get("subject")
    ])
    if params.get("register_1mm"):
        cargs.append("--1")
    if params.get("output") is not None:
        cargs.extend([
            "--o",
            params.get("output")
        ])
    if params.get("symmetric"):
        cargs.append("--sym")
    if params.get("save_volume"):
        cargs.append("--save-vol")
    return cargs


def mni152reg_outputs(
    params: Mni152regParameters,
    execution: Execution,
) -> Mni152regOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Mni152regOutputs(
        root=execution.output_file("."),
        reg_matrix_2mm=execution.output_file("$SUBJECTS_DIR/" + params.get("subject") + "/mri/transforms/reg.mni152.2mm.dat"),
        reg_matrix_1mm=execution.output_file("$SUBJECTS_DIR/" + params.get("subject") + "/mri/transforms/reg.mni152.1mm.dat"),
    )
    return ret


def mni152reg_execute(
    params: Mni152regParameters,
    execution: Execution,
) -> Mni152regOutputs:
    """
    Registers the FreeSurfer subject to the FSL MNI 152 brain to create a
    tkregister-style registration matrix.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Mni152regOutputs`).
    """
    params = execution.params(params)
    cargs = mni152reg_cargs(params, execution)
    ret = mni152reg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mni152reg(
    subject: str,
    register_1mm: bool = False,
    output: str | None = None,
    symmetric: bool = False,
    save_volume: bool = False,
    runner: Runner | None = None,
) -> Mni152regOutputs:
    """
    Registers the FreeSurfer subject to the FSL MNI 152 brain to create a
    tkregister-style registration matrix.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: FreeSurfer subject ID.
        register_1mm: Register to 1mm target (instead of 2mm).
        output: Explicitly set output registration file.
        symmetric: Register to FSL symmetric target.
        save_volume: Sample original to output space.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Mni152regOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MNI152REG_METADATA)
    params = mni152reg_params(
        subject=subject,
        register_1mm=register_1mm,
        output=output,
        symmetric=symmetric,
        save_volume=save_volume,
    )
    return mni152reg_execute(params, execution)


__all__ = [
    "MNI152REG_METADATA",
    "Mni152regOutputs",
    "Mni152regParameters",
    "mni152reg",
    "mni152reg_params",
]
