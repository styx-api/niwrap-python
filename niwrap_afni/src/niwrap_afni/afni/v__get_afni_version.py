# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__GET_AFNI_VERSION_METADATA = Metadata(
    id="bb51d1e48d98267f36f879d9daa6a5cd5f703a6f.boutiques",
    name="@get.afni.version",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VGetAfniVersionParameters = typing.TypedDict('VGetAfniVersionParameters', {
    "__STYX_TYPE__": typing.Literal["@get.afni.version"],
    "version": str,
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
        "@get.afni.version": v__get_afni_version_cargs,
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
        "@get.afni.version": v__get_afni_version_outputs,
    }.get(t)


class VGetAfniVersionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__get_afni_version(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    src_dir: OutputPathType
    """Directory containing the downloaded AFNI source code for the specified
    version."""


def v__get_afni_version_params(
    version: str,
) -> VGetAfniVersionParameters:
    """
    Build parameters.
    
    Args:
        version: AFNI version number to get (e.g., 16.0.01).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@get.afni.version",
        "version": version,
    }
    return params


def v__get_afni_version_cargs(
    params: VGetAfniVersionParameters,
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
    cargs.append("@get.afni.version")
    cargs.append(params.get("version"))
    return cargs


def v__get_afni_version_outputs(
    params: VGetAfniVersionParameters,
    execution: Execution,
) -> VGetAfniVersionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VGetAfniVersionOutputs(
        root=execution.output_file("."),
        src_dir=execution.output_file("AFNI_" + params.get("version") + "/AFNI/src"),
    )
    return ret


def v__get_afni_version_execute(
    params: VGetAfniVersionParameters,
    execution: Execution,
) -> VGetAfniVersionOutputs:
    """
    Downloads the source code for a specified AFNI version.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VGetAfniVersionOutputs`).
    """
    params = execution.params(params)
    cargs = v__get_afni_version_cargs(params, execution)
    ret = v__get_afni_version_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__get_afni_version(
    version: str,
    runner: Runner | None = None,
) -> VGetAfniVersionOutputs:
    """
    Downloads the source code for a specified AFNI version.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        version: AFNI version number to get (e.g., 16.0.01).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGetAfniVersionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GET_AFNI_VERSION_METADATA)
    params = v__get_afni_version_params(
        version=version,
    )
    return v__get_afni_version_execute(params, execution)


__all__ = [
    "VGetAfniVersionOutputs",
    "VGetAfniVersionParameters",
    "V__GET_AFNI_VERSION_METADATA",
    "v__get_afni_version",
    "v__get_afni_version_params",
]
