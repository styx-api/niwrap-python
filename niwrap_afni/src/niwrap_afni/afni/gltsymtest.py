# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GLTSYMTEST_METADATA = Metadata(
    id="cb3ce3fd8a02c860741465a6388d7e399c05c7bb.boutiques",
    name="GLTsymtest",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


GltsymtestParameters = typing.TypedDict('GltsymtestParameters', {
    "__STYX_TYPE__": typing.Literal["GLTsymtest"],
    "badonly": bool,
    "varlist": str,
    "expr": list[str],
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
        "GLTsymtest": gltsymtest_cargs,
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


class GltsymtestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gltsymtest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def gltsymtest_params(
    varlist: str,
    expr: list[str],
    badonly: bool = False,
) -> GltsymtestParameters:
    """
    Build parameters.
    
    Args:
        varlist: A list of allowed variable names in the expression, separated\
            by commas, semicolons, and/or spaces.
        expr: GLT symbolic expression(s), enclosed in quotes.
        badonly: A flag to only output BAD messages rather than all messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "GLTsymtest",
        "badonly": badonly,
        "varlist": varlist,
        "expr": expr,
    }
    return params


def gltsymtest_cargs(
    params: GltsymtestParameters,
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
    cargs.append("GLTsymtest")
    if params.get("badonly"):
        cargs.append("-badonly")
    cargs.append(params.get("varlist"))
    cargs.extend(params.get("expr"))
    return cargs


def gltsymtest_outputs(
    params: GltsymtestParameters,
    execution: Execution,
) -> GltsymtestOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GltsymtestOutputs(
        root=execution.output_file("."),
    )
    return ret


def gltsymtest_execute(
    params: GltsymtestParameters,
    execution: Execution,
) -> GltsymtestOutputs:
    """
    A tool to test the validity of '-gltsym' strings for use with 3dDeconvolve or
    3dREMLfit.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GltsymtestOutputs`).
    """
    params = execution.params(params)
    cargs = gltsymtest_cargs(params, execution)
    ret = gltsymtest_outputs(params, execution)
    execution.run(cargs)
    return ret


def gltsymtest(
    varlist: str,
    expr: list[str],
    badonly: bool = False,
    runner: Runner | None = None,
) -> GltsymtestOutputs:
    """
    A tool to test the validity of '-gltsym' strings for use with 3dDeconvolve or
    3dREMLfit.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        varlist: A list of allowed variable names in the expression, separated\
            by commas, semicolons, and/or spaces.
        expr: GLT symbolic expression(s), enclosed in quotes.
        badonly: A flag to only output BAD messages rather than all messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GltsymtestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GLTSYMTEST_METADATA)
    params = gltsymtest_params(
        badonly=badonly,
        varlist=varlist,
        expr=expr,
    )
    return gltsymtest_execute(params, execution)


__all__ = [
    "GLTSYMTEST_METADATA",
    "GltsymtestOutputs",
    "GltsymtestParameters",
    "gltsymtest",
    "gltsymtest_params",
]
