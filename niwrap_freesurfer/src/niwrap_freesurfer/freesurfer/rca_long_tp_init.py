# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RCA_LONG_TP_INIT_METADATA = Metadata(
    id="1ba25741004958df03ca6fd11c8637b4fcf2ca35.boutiques",
    name="rca-long-tp-init",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


RcaLongTpInitParameters = typing.TypedDict('RcaLongTpInitParameters', {
    "__STYX_TYPE__": typing.Literal["rca-long-tp-init"],
    "timepoint": str,
    "base": str,
    "use_long_base_ctrl_vol": bool,
    "hemisphere": typing.NotRequired[typing.Literal["lh", "rh"] | None],
    "expert_opts": typing.NotRequired[InputPathType | None],
    "subject": typing.NotRequired[str | None],
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
        "rca-long-tp-init": rca_long_tp_init_cargs,
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


class RcaLongTpInitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rca_long_tp_init(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rca_long_tp_init_params(
    timepoint: str,
    base: str,
    use_long_base_ctrl_vol: bool = False,
    hemisphere: typing.Literal["lh", "rh"] | None = None,
    expert_opts: InputPathType | None = None,
    subject: str | None = None,
) -> RcaLongTpInitParameters:
    """
    Build parameters.
    
    Args:
        timepoint: Timepoint identifier.
        base: Base identifier.
        use_long_base_ctrl_vol: Use long base control volume.
        hemisphere: Specify the hemisphere (left or right).
        expert_opts: Expert options file.
        subject: Subject identifier for testing; put after -long.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rca-long-tp-init",
        "timepoint": timepoint,
        "base": base,
        "use_long_base_ctrl_vol": use_long_base_ctrl_vol,
    }
    if hemisphere is not None:
        params["hemisphere"] = hemisphere
    if expert_opts is not None:
        params["expert_opts"] = expert_opts
    if subject is not None:
        params["subject"] = subject
    return params


def rca_long_tp_init_cargs(
    params: RcaLongTpInitParameters,
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
    cargs.append("rca-long-tp-init")
    cargs.extend([
        "-long",
        params.get("timepoint")
    ])
    cargs.append(params.get("base"))
    if params.get("use_long_base_ctrl_vol"):
        cargs.append("-uselongbasectrlvol")
    if params.get("hemisphere") is not None:
        cargs.extend([
            "-hemi",
            params.get("hemisphere")
        ])
    if params.get("expert_opts") is not None:
        cargs.extend([
            "-expert",
            execution.input_file(params.get("expert_opts"))
        ])
    if params.get("subject") is not None:
        cargs.extend([
            "-s",
            params.get("subject")
        ])
    return cargs


def rca_long_tp_init_outputs(
    params: RcaLongTpInitParameters,
    execution: Execution,
) -> RcaLongTpInitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RcaLongTpInitOutputs(
        root=execution.output_file("."),
    )
    return ret


def rca_long_tp_init_execute(
    params: RcaLongTpInitParameters,
    execution: Execution,
) -> RcaLongTpInitOutputs:
    """
    Initialize long timepoint subject for recon-all processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RcaLongTpInitOutputs`).
    """
    params = execution.params(params)
    cargs = rca_long_tp_init_cargs(params, execution)
    ret = rca_long_tp_init_outputs(params, execution)
    execution.run(cargs)
    return ret


def rca_long_tp_init(
    timepoint: str,
    base: str,
    use_long_base_ctrl_vol: bool = False,
    hemisphere: typing.Literal["lh", "rh"] | None = None,
    expert_opts: InputPathType | None = None,
    subject: str | None = None,
    runner: Runner | None = None,
) -> RcaLongTpInitOutputs:
    """
    Initialize long timepoint subject for recon-all processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        timepoint: Timepoint identifier.
        base: Base identifier.
        use_long_base_ctrl_vol: Use long base control volume.
        hemisphere: Specify the hemisphere (left or right).
        expert_opts: Expert options file.
        subject: Subject identifier for testing; put after -long.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RcaLongTpInitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RCA_LONG_TP_INIT_METADATA)
    params = rca_long_tp_init_params(
        timepoint=timepoint,
        base=base,
        use_long_base_ctrl_vol=use_long_base_ctrl_vol,
        hemisphere=hemisphere,
        expert_opts=expert_opts,
        subject=subject,
    )
    return rca_long_tp_init_execute(params, execution)


__all__ = [
    "RCA_LONG_TP_INIT_METADATA",
    "RcaLongTpInitOutputs",
    "RcaLongTpInitParameters",
    "rca_long_tp_init",
    "rca_long_tp_init_params",
]
