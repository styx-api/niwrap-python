# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SCRIPT_CHECK_METADATA = Metadata(
    id="d81cacac508059d0cecc8bef5d4a8425946e1d54.boutiques",
    name="@ScriptCheck",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VScriptCheckParameters = typing.TypedDict('VScriptCheckParameters', {
    "__STYXTYPE__": typing.Literal["@ScriptCheck"],
    "clean": bool,
    "suffix": typing.NotRequired[str | None],
    "scripts": list[InputPathType],
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
        "@ScriptCheck": v__script_check_cargs,
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
        "@ScriptCheck": v__script_check_outputs,
    }.get(t)


class VScriptCheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__script_check(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    uncleaned_file: OutputPathType
    """Uncleaned original file with specified suffix"""
    cleaned_file: OutputPathType
    """Cleaned file if -clean option is used"""


def v__script_check_params(
    scripts: list[InputPathType],
    clean: bool = False,
    suffix: str | None = None,
) -> VScriptCheckParameters:
    """
    Build parameters.
    
    Args:
        scripts: Scripts to be checked for improperly terminated lines.
        clean: Clean bad line breaks.
        suffix: Rename uncleaned file with specified suffix. Default is .uncln.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ScriptCheck",
        "clean": clean,
        "scripts": scripts,
    }
    if suffix is not None:
        params["suffix"] = suffix
    return params


def v__script_check_cargs(
    params: VScriptCheckParameters,
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
    cargs.append("@ScriptCheck")
    if params.get("clean"):
        cargs.append("-clean")
    if params.get("suffix") is not None:
        cargs.extend([
            "-suffix",
            params.get("suffix")
        ])
    cargs.extend([execution.input_file(f) for f in params.get("scripts")])
    return cargs


def v__script_check_outputs(
    params: VScriptCheckParameters,
    execution: Execution,
) -> VScriptCheckOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VScriptCheckOutputs(
        root=execution.output_file("."),
        uncleaned_file=execution.output_file("{SCRIPT}.uncln"),
        cleaned_file=execution.output_file("{SCRIPT}"),
    )
    return ret


def v__script_check_execute(
    params: VScriptCheckParameters,
    execution: Execution,
) -> VScriptCheckOutputs:
    """
    Checks scripts for improperly terminated lines and optionally cleans them.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VScriptCheckOutputs`).
    """
    params = execution.params(params)
    cargs = v__script_check_cargs(params, execution)
    ret = v__script_check_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__script_check(
    scripts: list[InputPathType],
    clean: bool = False,
    suffix: str | None = None,
    runner: Runner | None = None,
) -> VScriptCheckOutputs:
    """
    Checks scripts for improperly terminated lines and optionally cleans them.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        scripts: Scripts to be checked for improperly terminated lines.
        clean: Clean bad line breaks.
        suffix: Rename uncleaned file with specified suffix. Default is .uncln.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VScriptCheckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SCRIPT_CHECK_METADATA)
    params = v__script_check_params(
        clean=clean,
        suffix=suffix,
        scripts=scripts,
    )
    return v__script_check_execute(params, execution)


__all__ = [
    "VScriptCheckOutputs",
    "VScriptCheckParameters",
    "V__SCRIPT_CHECK_METADATA",
    "v__script_check",
    "v__script_check_params",
]
