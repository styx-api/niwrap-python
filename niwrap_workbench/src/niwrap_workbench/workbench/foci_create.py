# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FOCI_CREATE_METADATA = Metadata(
    id="b44d5a5c475f62b461f92b071ae7cead58a1f1d0.boutiques",
    name="foci-create",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


FociCreateClassParameters = typing.TypedDict('FociCreateClassParameters', {
    "__STYX_TYPE__": typing.Literal["class"],
    "class_name": str,
    "foci_list_file": str,
    "surface": InputPathType,
})


FociCreateParameters = typing.TypedDict('FociCreateParameters', {
    "__STYX_TYPE__": typing.Literal["foci-create"],
    "output": str,
    "class": typing.NotRequired[list[FociCreateClassParameters] | None],
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
        "foci-create": foci_create_cargs,
        "class": foci_create_class_cargs,
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
        "foci-create": foci_create_outputs,
    }.get(t)


def foci_create_class_params(
    class_name: str,
    foci_list_file: str,
    surface: InputPathType,
) -> FociCreateClassParameters:
    """
    Build parameters.
    
    Args:
        class_name: name of class.
        foci_list_file: text file containing foci names, coordinates, and\
            colors.
        surface: surface file for projection of foci list file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "class",
        "class_name": class_name,
        "foci_list_file": foci_list_file,
        "surface": surface,
    }
    return params


def foci_create_class_cargs(
    params: FociCreateClassParameters,
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
    cargs.append("-class")
    cargs.append(params.get("class_name"))
    cargs.append(params.get("foci_list_file"))
    cargs.append(execution.input_file(params.get("surface")))
    return cargs


class FociCreateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `foci_create(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output foci file"""


def foci_create_params(
    output: str,
    class_: list[FociCreateClassParameters] | None = None,
) -> FociCreateParameters:
    """
    Build parameters.
    
    Args:
        output: the output foci file.
        class_: specify class input data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "foci-create",
        "output": output,
    }
    if class_ is not None:
        params["class"] = class_
    return params


def foci_create_cargs(
    params: FociCreateParameters,
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
    cargs.append("wb_command")
    cargs.append("-foci-create")
    cargs.append(params.get("output"))
    if params.get("class") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("class")] for a in c])
    return cargs


def foci_create_outputs(
    params: FociCreateParameters,
    execution: Execution,
) -> FociCreateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FociCreateOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def foci_create_execute(
    params: FociCreateParameters,
    execution: Execution,
) -> FociCreateOutputs:
    """
    Create a foci file.
    
    Creates a foci file from names, coordinates, and RGB values in a text file.
    The text file must have the following format (2 lines per focus):
    
    <focus-name>
    <red> <green> <blue> <x> <y> <z>
    ...
    
    Foci names are specified on a separate line from their coordinates and
    color, in order to let foci names contain spaces. Whitespace is trimmed from
    both ends of the foci name, but is kept if it is in the middle of a name.
    The values of <red>, <green>, <blue> and must be integers from 0 to 255, and
    will specify the color the foci is drawn as.
    
    Foci are grouped into classes and the name for the class is specified using
    the <class-name> parameter.
    
    All foci within one text file must be associated with the structure
    contained in the <surface> parameter and are projected to that surface.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FociCreateOutputs`).
    """
    params = execution.params(params)
    cargs = foci_create_cargs(params, execution)
    ret = foci_create_outputs(params, execution)
    execution.run(cargs)
    return ret


def foci_create(
    output: str,
    class_: list[FociCreateClassParameters] | None = None,
    runner: Runner | None = None,
) -> FociCreateOutputs:
    """
    Create a foci file.
    
    Creates a foci file from names, coordinates, and RGB values in a text file.
    The text file must have the following format (2 lines per focus):
    
    <focus-name>
    <red> <green> <blue> <x> <y> <z>
    ...
    
    Foci names are specified on a separate line from their coordinates and
    color, in order to let foci names contain spaces. Whitespace is trimmed from
    both ends of the foci name, but is kept if it is in the middle of a name.
    The values of <red>, <green>, <blue> and must be integers from 0 to 255, and
    will specify the color the foci is drawn as.
    
    Foci are grouped into classes and the name for the class is specified using
    the <class-name> parameter.
    
    All foci within one text file must be associated with the structure
    contained in the <surface> parameter and are projected to that surface.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        output: the output foci file.
        class_: specify class input data.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FociCreateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOCI_CREATE_METADATA)
    params = foci_create_params(
        output=output,
        class_=class_,
    )
    return foci_create_execute(params, execution)


__all__ = [
    "FOCI_CREATE_METADATA",
    "FociCreateClassParameters",
    "FociCreateOutputs",
    "FociCreateParameters",
    "foci_create",
    "foci_create_class_params",
    "foci_create_params",
]
