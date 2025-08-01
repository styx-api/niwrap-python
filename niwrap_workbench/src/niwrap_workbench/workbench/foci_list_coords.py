# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FOCI_LIST_COORDS_METADATA = Metadata(
    id="22d2987788299a371745940b65548a5143218377.boutiques",
    name="foci-list-coords",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


FociListCoordsParameters = typing.TypedDict('FociListCoordsParameters', {
    "__STYXTYPE__": typing.Literal["foci-list-coords"],
    "foci_file": InputPathType,
    "coord_file_out": str,
    "opt_names_out_names_file_out": typing.NotRequired[str | None],
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
        "foci-list-coords": foci_list_coords_cargs,
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


class FociListCoordsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `foci_list_coords(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def foci_list_coords_params(
    foci_file: InputPathType,
    coord_file_out: str,
    opt_names_out_names_file_out: str | None = None,
) -> FociListCoordsParameters:
    """
    Build parameters.
    
    Args:
        foci_file: input foci file.
        coord_file_out: output - the output coordinate text file.
        opt_names_out_names_file_out: output the foci names: output - text file\
            to put foci names in.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "foci-list-coords",
        "foci_file": foci_file,
        "coord_file_out": coord_file_out,
    }
    if opt_names_out_names_file_out is not None:
        params["opt_names_out_names_file_out"] = opt_names_out_names_file_out
    return params


def foci_list_coords_cargs(
    params: FociListCoordsParameters,
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
    cargs.append("-foci-list-coords")
    cargs.append(execution.input_file(params.get("foci_file")))
    cargs.append(params.get("coord_file_out"))
    if params.get("opt_names_out_names_file_out") is not None:
        cargs.extend([
            "-names-out",
            params.get("opt_names_out_names_file_out")
        ])
    return cargs


def foci_list_coords_outputs(
    params: FociListCoordsParameters,
    execution: Execution,
) -> FociListCoordsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FociListCoordsOutputs(
        root=execution.output_file("."),
    )
    return ret


def foci_list_coords_execute(
    params: FociListCoordsParameters,
    execution: Execution,
) -> FociListCoordsOutputs:
    """
    Output foci coordinates in a text file.
    
    Output the coordinates for every focus in the foci file, and optionally the
    focus names in a second text file.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FociListCoordsOutputs`).
    """
    params = execution.params(params)
    cargs = foci_list_coords_cargs(params, execution)
    ret = foci_list_coords_outputs(params, execution)
    execution.run(cargs)
    return ret


def foci_list_coords(
    foci_file: InputPathType,
    coord_file_out: str,
    opt_names_out_names_file_out: str | None = None,
    runner: Runner | None = None,
) -> FociListCoordsOutputs:
    """
    Output foci coordinates in a text file.
    
    Output the coordinates for every focus in the foci file, and optionally the
    focus names in a second text file.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        foci_file: input foci file.
        coord_file_out: output - the output coordinate text file.
        opt_names_out_names_file_out: output the foci names: output - text file\
            to put foci names in.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FociListCoordsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOCI_LIST_COORDS_METADATA)
    params = foci_list_coords_params(
        foci_file=foci_file,
        coord_file_out=coord_file_out,
        opt_names_out_names_file_out=opt_names_out_names_file_out,
    )
    return foci_list_coords_execute(params, execution)


__all__ = [
    "FOCI_LIST_COORDS_METADATA",
    "FociListCoordsOutputs",
    "FociListCoordsParameters",
    "foci_list_coords",
    "foci_list_coords_params",
]
