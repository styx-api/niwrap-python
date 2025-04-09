# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__MOVE_TO_SERIES_DIRS_METADATA = Metadata(
    id="3258c3e5be037bd2af4e822c7e7ad229a6157990.boutiques",
    name="@move.to.series.dirs",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VMoveToSeriesDirsParameters = typing.TypedDict('VMoveToSeriesDirsParameters', {
    "__STYX_TYPE__": typing.Literal["@move.to.series.dirs"],
    "action": typing.NotRequired[typing.Literal["copy", "move"] | None],
    "dprefix": typing.NotRequired[str | None],
    "tag": typing.NotRequired[str | None],
    "test": bool,
    "help": bool,
    "hist": bool,
    "ver": bool,
    "dicom_files": list[InputPathType],
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
        "@move.to.series.dirs": v__move_to_series_dirs_cargs,
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


class VMoveToSeriesDirsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__move_to_series_dirs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__move_to_series_dirs_params(
    dicom_files: list[InputPathType],
    action: typing.Literal["copy", "move"] | None = None,
    dprefix: str | None = None,
    tag: str | None = None,
    test: bool = False,
    help_: bool = False,
    hist: bool = False,
    ver: bool = False,
) -> VMoveToSeriesDirsParameters:
    """
    Build parameters.
    
    Args:
        dicom_files: Specify input DICOM files (e.g., IMG*).
        action: Specify action to perform: copy or move. Default is copy.
        dprefix: Specify directory root for output series directories. Default\
            is current directory.
        tag: Specify the DICOM tag to use for partitioning. Default is\
            0020,0011 (REL Series Number).
        test: Run in test mode, only show what would be done without actually\
            moving any files.
        help_: Show help information.
        hist: Show modification history.
        ver: Show version number.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@move.to.series.dirs",
        "test": test,
        "help": help_,
        "hist": hist,
        "ver": ver,
        "dicom_files": dicom_files,
    }
    if action is not None:
        params["action"] = action
    if dprefix is not None:
        params["dprefix"] = dprefix
    if tag is not None:
        params["tag"] = tag
    return params


def v__move_to_series_dirs_cargs(
    params: VMoveToSeriesDirsParameters,
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
    cargs.append("@move.to.series.dirs")
    if params.get("action") is not None:
        cargs.extend([
            "-action",
            params.get("action")
        ])
    if params.get("dprefix") is not None:
        cargs.extend([
            "-dprefix",
            params.get("dprefix")
        ])
    if params.get("tag") is not None:
        cargs.extend([
            "-tag",
            params.get("tag")
        ])
    if params.get("test"):
        cargs.append("-test")
    if params.get("help"):
        cargs.append("-help")
    if params.get("hist"):
        cargs.append("-hist")
    if params.get("ver"):
        cargs.append("-ver")
    cargs.extend([execution.input_file(f) for f in params.get("dicom_files")])
    return cargs


def v__move_to_series_dirs_outputs(
    params: VMoveToSeriesDirsParameters,
    execution: Execution,
) -> VMoveToSeriesDirsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VMoveToSeriesDirsOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__move_to_series_dirs_execute(
    params: VMoveToSeriesDirsParameters,
    execution: Execution,
) -> VMoveToSeriesDirsOutputs:
    """
    Partition DICOM files into series directories by copying or moving them to new
    series directories.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VMoveToSeriesDirsOutputs`).
    """
    params = execution.params(params)
    cargs = v__move_to_series_dirs_cargs(params, execution)
    ret = v__move_to_series_dirs_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__move_to_series_dirs(
    dicom_files: list[InputPathType],
    action: typing.Literal["copy", "move"] | None = None,
    dprefix: str | None = None,
    tag: str | None = None,
    test: bool = False,
    help_: bool = False,
    hist: bool = False,
    ver: bool = False,
    runner: Runner | None = None,
) -> VMoveToSeriesDirsOutputs:
    """
    Partition DICOM files into series directories by copying or moving them to new
    series directories.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dicom_files: Specify input DICOM files (e.g., IMG*).
        action: Specify action to perform: copy or move. Default is copy.
        dprefix: Specify directory root for output series directories. Default\
            is current directory.
        tag: Specify the DICOM tag to use for partitioning. Default is\
            0020,0011 (REL Series Number).
        test: Run in test mode, only show what would be done without actually\
            moving any files.
        help_: Show help information.
        hist: Show modification history.
        ver: Show version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VMoveToSeriesDirsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__MOVE_TO_SERIES_DIRS_METADATA)
    params = v__move_to_series_dirs_params(
        action=action,
        dprefix=dprefix,
        tag=tag,
        test=test,
        help_=help_,
        hist=hist,
        ver=ver,
        dicom_files=dicom_files,
    )
    return v__move_to_series_dirs_execute(params, execution)


__all__ = [
    "VMoveToSeriesDirsOutputs",
    "VMoveToSeriesDirsParameters",
    "V__MOVE_TO_SERIES_DIRS_METADATA",
    "v__move_to_series_dirs",
    "v__move_to_series_dirs_params",
]
