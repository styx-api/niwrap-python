# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

XSANATREG_METADATA = Metadata(
    id="92e3106d67a2897fb7d26ce43be63611d67973c8.boutiques",
    name="xsanatreg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


XsanatregParameters = typing.TypedDict('XsanatregParameters', {
    "__STYXTYPE__": typing.Literal["xsanatreg"],
    "src_cordir": str,
    "targ_cordir": str,
    "transform_file": str,
    "temp_directory": typing.NotRequired[str | None],
    "source_minc": typing.NotRequired[str | None],
    "target_minc": typing.NotRequired[str | None],
    "no_cleanup": bool,
    "version": bool,
    "umask": typing.NotRequired[str | None],
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
        "xsanatreg": xsanatreg_cargs,
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


class XsanatregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xsanatreg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def xsanatreg_params(
    src_cordir: str,
    targ_cordir: str,
    transform_file: str,
    temp_directory: str | None = None,
    source_minc: str | None = None,
    target_minc: str | None = None,
    no_cleanup: bool = False,
    version: bool = False,
    umask: str | None = None,
) -> XsanatregParameters:
    """
    Build parameters.
    
    Args:
        src_cordir: Directory of source COR volume.
        targ_cordir: Directory of target COR volume.
        transform_file: File in which to store the transformation.
        temp_directory: Directory for temporary storage, defaults to /tmp.
        source_minc: File name for source minc, set automatically if not\
            specified.
        target_minc: File name for target minc, set automatically if not\
            specified.
        no_cleanup: Do not delete temporary minc files.
        version: Print version and exit.
        umask: Set file mode creation mask.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "xsanatreg",
        "src_cordir": src_cordir,
        "targ_cordir": targ_cordir,
        "transform_file": transform_file,
        "no_cleanup": no_cleanup,
        "version": version,
    }
    if temp_directory is not None:
        params["temp_directory"] = temp_directory
    if source_minc is not None:
        params["source_minc"] = source_minc
    if target_minc is not None:
        params["target_minc"] = target_minc
    if umask is not None:
        params["umask"] = umask
    return params


def xsanatreg_cargs(
    params: XsanatregParameters,
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
    cargs.append("xsanatreg")
    cargs.extend([
        "-src",
        params.get("src_cordir")
    ])
    cargs.extend([
        "-targ",
        params.get("targ_cordir")
    ])
    cargs.extend([
        "-xfm",
        params.get("transform_file")
    ])
    if params.get("temp_directory") is not None:
        cargs.extend([
            "-tmpdir",
            params.get("temp_directory")
        ])
    if params.get("source_minc") is not None:
        cargs.extend([
            "-srcminc",
            params.get("source_minc")
        ])
    if params.get("target_minc") is not None:
        cargs.extend([
            "-targminc",
            params.get("target_minc")
        ])
    if params.get("no_cleanup"):
        cargs.append("-nocleanup")
    if params.get("version"):
        cargs.append("-version")
    if params.get("umask") is not None:
        cargs.extend([
            "-umask",
            params.get("umask")
        ])
    return cargs


def xsanatreg_outputs(
    params: XsanatregParameters,
    execution: Execution,
) -> XsanatregOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = XsanatregOutputs(
        root=execution.output_file("."),
    )
    return ret


def xsanatreg_execute(
    params: XsanatregParameters,
    execution: Execution,
) -> XsanatregOutputs:
    """
    A tool for registering source and target COR volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `XsanatregOutputs`).
    """
    params = execution.params(params)
    cargs = xsanatreg_cargs(params, execution)
    ret = xsanatreg_outputs(params, execution)
    execution.run(cargs)
    return ret


def xsanatreg(
    src_cordir: str,
    targ_cordir: str,
    transform_file: str,
    temp_directory: str | None = None,
    source_minc: str | None = None,
    target_minc: str | None = None,
    no_cleanup: bool = False,
    version: bool = False,
    umask: str | None = None,
    runner: Runner | None = None,
) -> XsanatregOutputs:
    """
    A tool for registering source and target COR volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        src_cordir: Directory of source COR volume.
        targ_cordir: Directory of target COR volume.
        transform_file: File in which to store the transformation.
        temp_directory: Directory for temporary storage, defaults to /tmp.
        source_minc: File name for source minc, set automatically if not\
            specified.
        target_minc: File name for target minc, set automatically if not\
            specified.
        no_cleanup: Do not delete temporary minc files.
        version: Print version and exit.
        umask: Set file mode creation mask.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XsanatregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XSANATREG_METADATA)
    params = xsanatreg_params(
        src_cordir=src_cordir,
        targ_cordir=targ_cordir,
        transform_file=transform_file,
        temp_directory=temp_directory,
        source_minc=source_minc,
        target_minc=target_minc,
        no_cleanup=no_cleanup,
        version=version,
        umask=umask,
    )
    return xsanatreg_execute(params, execution)


__all__ = [
    "XSANATREG_METADATA",
    "XsanatregOutputs",
    "XsanatregParameters",
    "xsanatreg",
    "xsanatreg_params",
]
