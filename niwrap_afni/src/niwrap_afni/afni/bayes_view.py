# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BAYES_VIEW_METADATA = Metadata(
    id="21ede4a2b31dfb05d448cf196912dc72f15188bb.boutiques",
    name="bayes_view",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


BayesViewParameters = typing.TypedDict('BayesViewParameters', {
    "__STYXTYPE__": typing.Literal["bayes_view"],
    "input_folder": str,
    "help": bool,
    "shiny_folder": typing.NotRequired[str | None],
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
        "bayes_view": bayes_view_cargs,
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


class BayesViewOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bayes_view(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def bayes_view_params(
    input_folder: str,
    help_: bool = False,
    shiny_folder: str | None = None,
) -> BayesViewParameters:
    """
    Build parameters.
    
    Args:
        input_folder: Path to a folder containing .RData files.
        help_: Show help message.
        shiny_folder: Use a custom shiny folder (for testing purposes).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bayes_view",
        "input_folder": input_folder,
        "help": help_,
    }
    if shiny_folder is not None:
        params["shiny_folder"] = shiny_folder
    return params


def bayes_view_cargs(
    params: BayesViewParameters,
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
    cargs.append("bayes_view")
    cargs.append(params.get("input_folder"))
    if params.get("help"):
        cargs.append("-help")
    if params.get("shiny_folder") is not None:
        cargs.extend([
            "-ShinyFolder",
            params.get("shiny_folder")
        ])
    return cargs


def bayes_view_outputs(
    params: BayesViewParameters,
    execution: Execution,
) -> BayesViewOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BayesViewOutputs(
        root=execution.output_file("."),
    )
    return ret


def bayes_view_execute(
    params: BayesViewParameters,
    execution: Execution,
) -> BayesViewOutputs:
    """
    Launch a shiny app to visualize RBA output files. The files must have the .RData
    extension.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BayesViewOutputs`).
    """
    params = execution.params(params)
    cargs = bayes_view_cargs(params, execution)
    ret = bayes_view_outputs(params, execution)
    execution.run(cargs)
    return ret


def bayes_view(
    input_folder: str,
    help_: bool = False,
    shiny_folder: str | None = None,
    runner: Runner | None = None,
) -> BayesViewOutputs:
    """
    Launch a shiny app to visualize RBA output files. The files must have the .RData
    extension.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_folder: Path to a folder containing .RData files.
        help_: Show help message.
        shiny_folder: Use a custom shiny folder (for testing purposes).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BayesViewOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BAYES_VIEW_METADATA)
    params = bayes_view_params(
        input_folder=input_folder,
        help_=help_,
        shiny_folder=shiny_folder,
    )
    return bayes_view_execute(params, execution)


__all__ = [
    "BAYES_VIEW_METADATA",
    "BayesViewOutputs",
    "BayesViewParameters",
    "bayes_view",
    "bayes_view_params",
]
