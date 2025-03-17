# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

UPDATE_NEEDED_METADATA = Metadata(
    id="bbeff96a804ee5f7f839128e9a8f2889e0e27e42.boutiques",
    name="UpdateNeeded",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


UpdateNeededParameters = typing.TypedDict('UpdateNeededParameters', {
    "__STYX_TYPE__": typing.Literal["UpdateNeeded"],
    "target_file": InputPathType,
    "source_file": InputPathType,
    "additional_source_files": typing.NotRequired[list[InputPathType] | None],
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
        "UpdateNeeded": update_needed_cargs,
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


class UpdateNeededOutputs(typing.NamedTuple):
    """
    Output object returned when calling `update_needed(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def update_needed_params(
    target_file: InputPathType,
    source_file: InputPathType,
    additional_source_files: list[InputPathType] | None = None,
) -> UpdateNeededParameters:
    """
    Build parameters.
    
    Args:
        target_file: The target file that needs to be updated.
        source_file: The primary source file for updating the target file.
        additional_source_files: Additional source files for updating the\
            target file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "UpdateNeeded",
        "target_file": target_file,
        "source_file": source_file,
    }
    if additional_source_files is not None:
        params["additional_source_files"] = additional_source_files
    return params


def update_needed_cargs(
    params: UpdateNeededParameters,
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
    cargs.append("UpdateNeeded")
    cargs.append(execution.input_file(params.get("target_file")))
    cargs.append(execution.input_file(params.get("source_file")))
    if params.get("additional_source_files") is not None:
        cargs.extend([execution.input_file(f) for f in params.get("additional_source_files")])
    return cargs


def update_needed_outputs(
    params: UpdateNeededParameters,
    execution: Execution,
) -> UpdateNeededOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = UpdateNeededOutputs(
        root=execution.output_file("."),
    )
    return ret


def update_needed_execute(
    params: UpdateNeededParameters,
    execution: Execution,
) -> UpdateNeededOutputs:
    """
    A command-line tool to update a target file based on one or more source files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `UpdateNeededOutputs`).
    """
    params = execution.params(params)
    cargs = update_needed_cargs(params, execution)
    ret = update_needed_outputs(params, execution)
    execution.run(cargs)
    return ret


def update_needed(
    target_file: InputPathType,
    source_file: InputPathType,
    additional_source_files: list[InputPathType] | None = None,
    runner: Runner | None = None,
) -> UpdateNeededOutputs:
    """
    A command-line tool to update a target file based on one or more source files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        target_file: The target file that needs to be updated.
        source_file: The primary source file for updating the target file.
        additional_source_files: Additional source files for updating the\
            target file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UpdateNeededOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UPDATE_NEEDED_METADATA)
    params = update_needed_params(
        target_file=target_file,
        source_file=source_file,
        additional_source_files=additional_source_files,
    )
    return update_needed_execute(params, execution)


__all__ = [
    "UPDATE_NEEDED_METADATA",
    "UpdateNeededOutputs",
    "UpdateNeededParameters",
    "update_needed",
    "update_needed_params",
]
