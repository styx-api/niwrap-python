# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PROMPT_POPUP_METADATA = Metadata(
    id="56ce96c081577f794f865f7030869659d97db1e1.boutiques",
    name="prompt_popup",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


PromptPopupParameters = typing.TypedDict('PromptPopupParameters', {
    "__STYX_TYPE__": typing.Literal["prompt_popup"],
    "message_pause": typing.NotRequired[str | None],
    "buttons_b": typing.NotRequired[list[str] | None],
    "timeout_to": typing.NotRequired[float | None],
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
        "prompt_popup": prompt_popup_cargs,
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


class PromptPopupOutputs(typing.NamedTuple):
    """
    Output object returned when calling `prompt_popup(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def prompt_popup_params(
    message_pause: str | None = None,
    buttons_b: list[str] | None = None,
    timeout_to: float | None = None,
) -> PromptPopupParameters:
    """
    Build parameters.
    
    Args:
        message_pause: Same as -message to match the old prompt_user.
        buttons_b: Same as -button.
        timeout_to: Same as -timeout TT.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "prompt_popup",
    }
    if message_pause is not None:
        params["message_pause"] = message_pause
    if buttons_b is not None:
        params["buttons_b"] = buttons_b
    if timeout_to is not None:
        params["timeout_to"] = timeout_to
    return params


def prompt_popup_cargs(
    params: PromptPopupParameters,
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
    cargs.append("prompt_popup")
    if params.get("message_pause") is not None:
        cargs.extend([
            "-pause",
            params.get("message_pause")
        ])
    if params.get("buttons_b") is not None:
        cargs.extend([
            "-b",
            *params.get("buttons_b")
        ])
    if params.get("timeout_to") is not None:
        cargs.extend([
            "-to",
            str(params.get("timeout_to"))
        ])
    return cargs


def prompt_popup_outputs(
    params: PromptPopupParameters,
    execution: Execution,
) -> PromptPopupOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PromptPopupOutputs(
        root=execution.output_file("."),
    )
    return ret


def prompt_popup_execute(
    params: PromptPopupParameters,
    execution: Execution,
) -> PromptPopupOutputs:
    """
    A command-line tool that pops up a window prompting user interaction with a
    message and buttons.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PromptPopupOutputs`).
    """
    params = execution.params(params)
    cargs = prompt_popup_cargs(params, execution)
    ret = prompt_popup_outputs(params, execution)
    execution.run(cargs)
    return ret


def prompt_popup(
    message_pause: str | None = None,
    buttons_b: list[str] | None = None,
    timeout_to: float | None = None,
    runner: Runner | None = None,
) -> PromptPopupOutputs:
    """
    A command-line tool that pops up a window prompting user interaction with a
    message and buttons.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        message_pause: Same as -message to match the old prompt_user.
        buttons_b: Same as -button.
        timeout_to: Same as -timeout TT.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PromptPopupOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PROMPT_POPUP_METADATA)
    params = prompt_popup_params(
        message_pause=message_pause,
        buttons_b=buttons_b,
        timeout_to=timeout_to,
    )
    return prompt_popup_execute(params, execution)


__all__ = [
    "PROMPT_POPUP_METADATA",
    "PromptPopupOutputs",
    "PromptPopupParameters",
    "prompt_popup",
    "prompt_popup_params",
]
