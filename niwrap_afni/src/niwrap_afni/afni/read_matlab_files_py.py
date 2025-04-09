# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

READ_MATLAB_FILES_PY_METADATA = Metadata(
    id="d93c09c43aac0af7cf212aad65ea83ad160cf02e.boutiques",
    name="read_matlab_files.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


ReadMatlabFilesPyParameters = typing.TypedDict('ReadMatlabFilesPyParameters', {
    "__STYX_TYPE__": typing.Literal["read_matlab_files.py"],
    "infiles": list[str],
    "prefix": typing.NotRequired[str | None],
    "overwrite": bool,
    "help": bool,
    "history": bool,
    "version": bool,
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
        "read_matlab_files.py": read_matlab_files_py_cargs,
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
        "read_matlab_files.py": read_matlab_files_py_outputs,
    }.get(t)


class ReadMatlabFilesPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `read_matlab_files_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    converted_1d_file: OutputPathType | None
    """Converted 1D format file"""


def read_matlab_files_py_params(
    infiles: list[str],
    prefix: str | None = None,
    overwrite: bool = False,
    help_: bool = False,
    history: bool = False,
    version: bool = False,
) -> ReadMatlabFilesPyParameters:
    """
    Build parameters.
    
    Args:
        infiles: Input MATLAB files to be processed.
        prefix: Prefix for output file names.
        overwrite: Overwrite any existing output files.
        help_: Show help message.
        history: Show revision history.
        version: Show version number.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "read_matlab_files.py",
        "infiles": infiles,
        "overwrite": overwrite,
        "help": help_,
        "history": history,
        "version": version,
    }
    if prefix is not None:
        params["prefix"] = prefix
    return params


def read_matlab_files_py_cargs(
    params: ReadMatlabFilesPyParameters,
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
    cargs.append("read_matlab_files.py")
    cargs.extend(params.get("infiles"))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("overwrite"):
        cargs.append("-overwrite")
    if params.get("help"):
        cargs.append("-help")
    if params.get("history"):
        cargs.append("-hist")
    if params.get("version"):
        cargs.append("-ver")
    return cargs


def read_matlab_files_py_outputs(
    params: ReadMatlabFilesPyParameters,
    execution: Execution,
) -> ReadMatlabFilesPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ReadMatlabFilesPyOutputs(
        root=execution.output_file("."),
        converted_1d_file=execution.output_file(params.get("prefix") + ".[INDEX].[KEY].1D") if (params.get("prefix") is not None) else None,
    )
    return ret


def read_matlab_files_py_execute(
    params: ReadMatlabFilesPyParameters,
    execution: Execution,
) -> ReadMatlabFilesPyOutputs:
    """
    Describe or convert MATLAB files (.mat) to 1D format.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ReadMatlabFilesPyOutputs`).
    """
    params = execution.params(params)
    cargs = read_matlab_files_py_cargs(params, execution)
    ret = read_matlab_files_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def read_matlab_files_py(
    infiles: list[str],
    prefix: str | None = None,
    overwrite: bool = False,
    help_: bool = False,
    history: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> ReadMatlabFilesPyOutputs:
    """
    Describe or convert MATLAB files (.mat) to 1D format.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infiles: Input MATLAB files to be processed.
        prefix: Prefix for output file names.
        overwrite: Overwrite any existing output files.
        help_: Show help message.
        history: Show revision history.
        version: Show version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReadMatlabFilesPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(READ_MATLAB_FILES_PY_METADATA)
    params = read_matlab_files_py_params(
        infiles=infiles,
        prefix=prefix,
        overwrite=overwrite,
        help_=help_,
        history=history,
        version=version,
    )
    return read_matlab_files_py_execute(params, execution)


__all__ = [
    "READ_MATLAB_FILES_PY_METADATA",
    "ReadMatlabFilesPyOutputs",
    "ReadMatlabFilesPyParameters",
    "read_matlab_files_py",
    "read_matlab_files_py_params",
]
