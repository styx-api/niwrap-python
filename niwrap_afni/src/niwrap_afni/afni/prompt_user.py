# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PROMPT_USER_METADATA = Metadata(
    id="50f7b3456cf7fa2cd699f8ebd295c575df5c9675.boutiques",
    name="prompt_user",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


PromptUserParameters = typing.TypedDict('PromptUserParameters', {
    "__STYX_TYPE__": typing.Literal["prompt_user"],
    "pause_message": str,
    "timeout": typing.NotRequired[float | None],
    "timeout_alias": typing.NotRequired[float | None],
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
        "prompt_user": prompt_user_cargs,
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


class PromptUserOutputs(typing.NamedTuple):
    """
    Output object returned when calling `prompt_user(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def prompt_user_params(
    pause_message: str,
    timeout: float | None = None,
    timeout_alias: float | None = None,
) -> PromptUserParameters:
    """
    Build parameters.
    
    Args:
        pause_message: Pops a window prompting the user with MESSAGE. If\
            MESSAGE is '-', it is read from stdin.
        timeout: Timeout in seconds for the prompt message. Default answer is\
            returned if TT seconds elapse without user input.
        timeout_alias: Alias for -timeout.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "prompt_user",
        "pause_message": pause_message,
    }
    if timeout is not None:
        params["timeout"] = timeout
    if timeout_alias is not None:
        params["timeout_alias"] = timeout_alias
    return params


def prompt_user_cargs(
    params: PromptUserParameters,
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
    cargs.append("prompt_user")
    cargs.extend([
        "<-pause>",
        params.get("pause_message")
    ])
    if params.get("timeout") is not None:
        cargs.extend([
            "-timeout",
            str(params.get("timeout"))
        ])
    if params.get("timeout_alias") is not None:
        cargs.extend([
            "-to",
            str(params.get("timeout_alias"))
        ])
    return cargs


def prompt_user_outputs(
    params: PromptUserParameters,
    execution: Execution,
) -> PromptUserOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PromptUserOutputs(
        root=execution.output_file("."),
    )
    return ret


def prompt_user_execute(
    params: PromptUserParameters,
    execution: Execution,
) -> PromptUserOutputs:
    """
    Tool that prompts a window requesting user input with a custom message.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PromptUserOutputs`).
    """
    params = execution.params(params)
    cargs = prompt_user_cargs(params, execution)
    ret = prompt_user_outputs(params, execution)
    execution.run(cargs)
    return ret


def prompt_user(
    pause_message: str,
    timeout: float | None = None,
    timeout_alias: float | None = None,
    runner: Runner | None = None,
) -> PromptUserOutputs:
    """
    Tool that prompts a window requesting user input with a custom message.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        pause_message: Pops a window prompting the user with MESSAGE. If\
            MESSAGE is '-', it is read from stdin.
        timeout: Timeout in seconds for the prompt message. Default answer is\
            returned if TT seconds elapse without user input.
        timeout_alias: Alias for -timeout.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PromptUserOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PROMPT_USER_METADATA)
    params = prompt_user_params(
        pause_message=pause_message,
        timeout=timeout,
        timeout_alias=timeout_alias,
    )
    return prompt_user_execute(params, execution)


__all__ = [
    "PROMPT_USER_METADATA",
    "PromptUserOutputs",
    "PromptUserParameters",
    "prompt_user",
    "prompt_user_params",
]
