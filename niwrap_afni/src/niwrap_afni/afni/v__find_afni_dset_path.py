# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__FIND_AFNI_DSET_PATH_METADATA = Metadata(
    id="d33aa66f6df6fbc7fea6bf4750fec389976226bb.boutiques",
    name="@FindAfniDsetPath",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VFindAfniDsetPathParameters = typing.TypedDict('VFindAfniDsetPathParameters', {
    "__STYX_TYPE__": typing.Literal["@FindAfniDsetPath"],
    "dsetname": str,
    "append_file": bool,
    "full_path": bool,
    "help": bool,
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
        "@FindAfniDsetPath": v__find_afni_dset_path_cargs,
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


class VFindAfniDsetPathOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__find_afni_dset_path(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__find_afni_dset_path_params(
    dsetname: str,
    append_file: bool = False,
    full_path: bool = False,
    help_: bool = False,
) -> VFindAfniDsetPathParameters:
    """
    Build parameters.
    
    Args:
        dsetname: Name of the dataset to search for.
        append_file: Show the file appended to (even with atlas name).
        full_path: Print full path instead of '.'.
        help_: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@FindAfniDsetPath",
        "dsetname": dsetname,
        "append_file": append_file,
        "full_path": full_path,
        "help": help_,
    }
    return params


def v__find_afni_dset_path_cargs(
    params: VFindAfniDsetPathParameters,
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
    cargs.append("@FindAfniDsetPath")
    cargs.append(params.get("dsetname"))
    if params.get("append_file"):
        cargs.append("-append_file")
    if params.get("full_path"):
        cargs.append("-full_path")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def v__find_afni_dset_path_outputs(
    params: VFindAfniDsetPathParameters,
    execution: Execution,
) -> VFindAfniDsetPathOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VFindAfniDsetPathOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__find_afni_dset_path_execute(
    params: VFindAfniDsetPathParameters,
    execution: Execution,
) -> VFindAfniDsetPathOutputs:
    """
    Searches various AFNI directories for a specified dataset and returns its path.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VFindAfniDsetPathOutputs`).
    """
    params = execution.params(params)
    cargs = v__find_afni_dset_path_cargs(params, execution)
    ret = v__find_afni_dset_path_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__find_afni_dset_path(
    dsetname: str,
    append_file: bool = False,
    full_path: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> VFindAfniDsetPathOutputs:
    """
    Searches various AFNI directories for a specified dataset and returns its path.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dsetname: Name of the dataset to search for.
        append_file: Show the file appended to (even with atlas name).
        full_path: Print full path instead of '.'.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFindAfniDsetPathOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FIND_AFNI_DSET_PATH_METADATA)
    params = v__find_afni_dset_path_params(
        dsetname=dsetname,
        append_file=append_file,
        full_path=full_path,
        help_=help_,
    )
    return v__find_afni_dset_path_execute(params, execution)


__all__ = [
    "VFindAfniDsetPathOutputs",
    "VFindAfniDsetPathParameters",
    "V__FIND_AFNI_DSET_PATH_METADATA",
    "v__find_afni_dset_path",
    "v__find_afni_dset_path_params",
]
