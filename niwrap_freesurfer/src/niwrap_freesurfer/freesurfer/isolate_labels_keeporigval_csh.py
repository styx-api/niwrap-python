# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ISOLATE_LABELS_KEEPORIGVAL_CSH_METADATA = Metadata(
    id="a6c0e69eb1ba1ff02a31f0459157a99e801ba645.boutiques",
    name="isolate_labels_keeporigval.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


IsolateLabelsKeeporigvalCshParameters = typing.TypedDict('IsolateLabelsKeeporigvalCshParameters', {
    "__STYX_TYPE__": typing.Literal["isolate_labels_keeporigval.csh"],
    "vol": InputPathType,
    "outprefix": str,
    "label": typing.NotRequired[str | None],
    "version": bool,
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
        "isolate_labels_keeporigval.csh": isolate_labels_keeporigval_csh_cargs,
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
        "isolate_labels_keeporigval.csh": isolate_labels_keeporigval_csh_outputs,
    }.get(t)


class IsolateLabelsKeeporigvalCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `isolate_labels_keeporigval_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_files: OutputPathType
    """Output binary label file(s)"""


def isolate_labels_keeporigval_csh_params(
    vol: InputPathType,
    outprefix: str,
    label: str | None = None,
    version: bool = False,
    help_: bool = False,
) -> IsolateLabelsKeeporigvalCshParameters:
    """
    Build parameters.
    
    Args:
        vol: Label volume to be analyzed.
        outprefix: Prefix for output binary label file(s).
        label: The particular label to be analyzed. By default, it is ALL\
            labels in the volume.
        version: Print version and exit.
        help_: Print help and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "isolate_labels_keeporigval.csh",
        "vol": vol,
        "outprefix": outprefix,
        "version": version,
        "help": help_,
    }
    if label is not None:
        params["label"] = label
    return params


def isolate_labels_keeporigval_csh_cargs(
    params: IsolateLabelsKeeporigvalCshParameters,
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
    cargs.append("isolate_labels_keeporigval.csh")
    cargs.extend([
        "--vol",
        execution.input_file(params.get("vol"))
    ])
    cargs.extend([
        "--outprefix",
        params.get("outprefix")
    ])
    if params.get("label") is not None:
        cargs.extend([
            "--l",
            params.get("label")
        ])
    if params.get("version"):
        cargs.append("--version")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def isolate_labels_keeporigval_csh_outputs(
    params: IsolateLabelsKeeporigvalCshParameters,
    execution: Execution,
) -> IsolateLabelsKeeporigvalCshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = IsolateLabelsKeeporigvalCshOutputs(
        root=execution.output_file("."),
        output_label_files=execution.output_file(params.get("outprefix") + "_label*.nii.gz"),
    )
    return ret


def isolate_labels_keeporigval_csh_execute(
    params: IsolateLabelsKeeporigvalCshParameters,
    execution: Execution,
) -> IsolateLabelsKeeporigvalCshOutputs:
    """
    Separates out a particular or all labels into individual binary files keeping
    the original label values for subsequent shape analysis.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `IsolateLabelsKeeporigvalCshOutputs`).
    """
    params = execution.params(params)
    cargs = isolate_labels_keeporigval_csh_cargs(params, execution)
    ret = isolate_labels_keeporigval_csh_outputs(params, execution)
    execution.run(cargs)
    return ret


def isolate_labels_keeporigval_csh(
    vol: InputPathType,
    outprefix: str,
    label: str | None = None,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> IsolateLabelsKeeporigvalCshOutputs:
    """
    Separates out a particular or all labels into individual binary files keeping
    the original label values for subsequent shape analysis.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        vol: Label volume to be analyzed.
        outprefix: Prefix for output binary label file(s).
        label: The particular label to be analyzed. By default, it is ALL\
            labels in the volume.
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IsolateLabelsKeeporigvalCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ISOLATE_LABELS_KEEPORIGVAL_CSH_METADATA)
    params = isolate_labels_keeporigval_csh_params(
        vol=vol,
        outprefix=outprefix,
        label=label,
        version=version,
        help_=help_,
    )
    return isolate_labels_keeporigval_csh_execute(params, execution)


__all__ = [
    "ISOLATE_LABELS_KEEPORIGVAL_CSH_METADATA",
    "IsolateLabelsKeeporigvalCshOutputs",
    "IsolateLabelsKeeporigvalCshParameters",
    "isolate_labels_keeporigval_csh",
    "isolate_labels_keeporigval_csh_params",
]
