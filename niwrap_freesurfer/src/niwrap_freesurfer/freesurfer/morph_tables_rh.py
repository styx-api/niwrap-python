# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MORPH_TABLES_RH_METADATA = Metadata(
    id="2f3add04b35d7726ca806ca38014821260043ebc.boutiques",
    name="morph_tables-rh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MorphTablesRhParameters = typing.TypedDict('MorphTablesRhParameters', {
    "__STYX_TYPE__": typing.Literal["morph_tables-rh"],
    "options": typing.NotRequired[str | None],
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
        "morph_tables-rh": morph_tables_rh_cargs,
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


class MorphTablesRhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_tables_rh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def morph_tables_rh_params(
    options: str | None = None,
) -> MorphTablesRhParameters:
    """
    Build parameters.
    
    Args:
        options: Options used by morph_tables-rh.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "morph_tables-rh",
    }
    if options is not None:
        params["options"] = options
    return params


def morph_tables_rh_cargs(
    params: MorphTablesRhParameters,
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
    if params.get("options") is not None:
        cargs.extend([
            "-rh",
            "morph_tables" + params.get("options")
        ])
    return cargs


def morph_tables_rh_outputs(
    params: MorphTablesRhParameters,
    execution: Execution,
) -> MorphTablesRhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MorphTablesRhOutputs(
        root=execution.output_file("."),
    )
    return ret


def morph_tables_rh_execute(
    params: MorphTablesRhParameters,
    execution: Execution,
) -> MorphTablesRhOutputs:
    """
    A tool from Freesurfer associated with morphological tables for the right
    hemisphere.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MorphTablesRhOutputs`).
    """
    params = execution.params(params)
    cargs = morph_tables_rh_cargs(params, execution)
    ret = morph_tables_rh_outputs(params, execution)
    execution.run(cargs)
    return ret


def morph_tables_rh(
    options: str | None = None,
    runner: Runner | None = None,
) -> MorphTablesRhOutputs:
    """
    A tool from Freesurfer associated with morphological tables for the right
    hemisphere.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        options: Options used by morph_tables-rh.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphTablesRhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_TABLES_RH_METADATA)
    params = morph_tables_rh_params(
        options=options,
    )
    return morph_tables_rh_execute(params, execution)


__all__ = [
    "MORPH_TABLES_RH_METADATA",
    "MorphTablesRhOutputs",
    "MorphTablesRhParameters",
    "morph_tables_rh",
    "morph_tables_rh_params",
]
