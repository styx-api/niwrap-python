# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REG_MNI305_2MM_METADATA = Metadata(
    id="baca96deead4a89fad3eca8defaa337786ee5cdf.boutiques",
    name="reg-mni305.2mm",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


RegMni3052mmParameters = typing.TypedDict('RegMni3052mmParameters', {
    "__STYX_TYPE__": typing.Literal["reg-mni305.2mm"],
    "subject_id": str,
    "regfile": InputPathType,
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
        "reg-mni305.2mm": reg_mni305_2mm_cargs,
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
        "reg-mni305.2mm": reg_mni305_2mm_outputs,
    }.get(t)


class RegMni3052mmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_mni305_2mm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_regfile: OutputPathType
    """tkregister2-style registration matrix output file."""


def reg_mni305_2mm_params(
    subject_id: str,
    regfile: InputPathType,
) -> RegMni3052mmParameters:
    """
    Build parameters.
    
    Args:
        subject_id: Subject ID for the FreeSurfer anatomical space.
        regfile: tkregister2-style registration matrix file (should have a .dat\
            or .reg extension).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "reg-mni305.2mm",
        "subject_id": subject_id,
        "regfile": regfile,
    }
    return params


def reg_mni305_2mm_cargs(
    params: RegMni3052mmParameters,
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
    cargs.append("reg-mni305.2mm")
    cargs.extend([
        "--s",
        params.get("subject_id")
    ])
    cargs.extend([
        "--reg",
        execution.input_file(params.get("regfile"))
    ])
    return cargs


def reg_mni305_2mm_outputs(
    params: RegMni3052mmParameters,
    execution: Execution,
) -> RegMni3052mmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RegMni3052mmOutputs(
        root=execution.output_file("."),
        output_regfile=execution.output_file(pathlib.Path(params.get("regfile")).name),
    )
    return ret


def reg_mni305_2mm_execute(
    params: RegMni3052mmParameters,
    execution: Execution,
) -> RegMni3052mmOutputs:
    """
    Computes the registration between the FreeSurfer MNI305 2mm space and a
    subject's FreeSurfer anatomical space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RegMni3052mmOutputs`).
    """
    params = execution.params(params)
    cargs = reg_mni305_2mm_cargs(params, execution)
    ret = reg_mni305_2mm_outputs(params, execution)
    execution.run(cargs)
    return ret


def reg_mni305_2mm(
    subject_id: str,
    regfile: InputPathType,
    runner: Runner | None = None,
) -> RegMni3052mmOutputs:
    """
    Computes the registration between the FreeSurfer MNI305 2mm space and a
    subject's FreeSurfer anatomical space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: Subject ID for the FreeSurfer anatomical space.
        regfile: tkregister2-style registration matrix file (should have a .dat\
            or .reg extension).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegMni3052mmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_MNI305_2MM_METADATA)
    params = reg_mni305_2mm_params(
        subject_id=subject_id,
        regfile=regfile,
    )
    return reg_mni305_2mm_execute(params, execution)


__all__ = [
    "REG_MNI305_2MM_METADATA",
    "RegMni3052mmOutputs",
    "RegMni3052mmParameters",
    "reg_mni305_2mm",
    "reg_mni305_2mm_params",
]
