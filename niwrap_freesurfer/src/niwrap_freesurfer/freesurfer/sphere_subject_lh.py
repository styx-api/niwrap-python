# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SPHERE_SUBJECT_LH_METADATA = Metadata(
    id="ff268b28a43fc5b537953764154fa43ebab2c033.boutiques",
    name="sphere_subject-lh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


SphereSubjectLhParameters = typing.TypedDict('SphereSubjectLhParameters', {
    "__STYX_TYPE__": typing.Literal["sphere_subject-lh"],
    "license_file": InputPathType,
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
        "sphere_subject-lh": sphere_subject_lh_cargs,
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


class SphereSubjectLhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sphere_subject_lh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def sphere_subject_lh_params(
    license_file: InputPathType,
) -> SphereSubjectLhParameters:
    """
    Build parameters.
    
    Args:
        license_file: Path to the FreeSurfer license file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sphere_subject-lh",
        "license_file": license_file,
    }
    return params


def sphere_subject_lh_cargs(
    params: SphereSubjectLhParameters,
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
    cargs.append("sphere_subject-lh")
    cargs.extend([
        "-lh",
        execution.input_file(params.get("license_file"))
    ])
    return cargs


def sphere_subject_lh_outputs(
    params: SphereSubjectLhParameters,
    execution: Execution,
) -> SphereSubjectLhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SphereSubjectLhOutputs(
        root=execution.output_file("."),
    )
    return ret


def sphere_subject_lh_execute(
    params: SphereSubjectLhParameters,
    execution: Execution,
) -> SphereSubjectLhOutputs:
    """
    Tool for processing spherical representations in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SphereSubjectLhOutputs`).
    """
    params = execution.params(params)
    cargs = sphere_subject_lh_cargs(params, execution)
    ret = sphere_subject_lh_outputs(params, execution)
    execution.run(cargs)
    return ret


def sphere_subject_lh(
    license_file: InputPathType,
    runner: Runner | None = None,
) -> SphereSubjectLhOutputs:
    """
    Tool for processing spherical representations in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        license_file: Path to the FreeSurfer license file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SphereSubjectLhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPHERE_SUBJECT_LH_METADATA)
    params = sphere_subject_lh_params(
        license_file=license_file,
    )
    return sphere_subject_lh_execute(params, execution)


__all__ = [
    "SPHERE_SUBJECT_LH_METADATA",
    "SphereSubjectLhOutputs",
    "SphereSubjectLhParameters",
    "sphere_subject_lh",
    "sphere_subject_lh_params",
]
