# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RECON_ALL_EXVIVO_METADATA = Metadata(
    id="9f00b252b2f61f947af4a725491db0b3cab46912.boutiques",
    name="recon-all-exvivo",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


ReconAllExvivoParameters = typing.TypedDict('ReconAllExvivoParameters', {
    "__STYX_TYPE__": typing.Literal["recon-all-exvivo"],
    "subject_id": str,
    "hemisphere": typing.NotRequired[str | None],
    "nocerebellum": bool,
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
        "recon-all-exvivo": recon_all_exvivo_cargs,
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


class ReconAllExvivoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `recon_all_exvivo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def recon_all_exvivo_params(
    subject_id: str,
    hemisphere: str | None = None,
    nocerebellum: bool = False,
) -> ReconAllExvivoParameters:
    """
    Build parameters.
    
    Args:
        subject_id: Subject identifier.
        hemisphere: Specify hemisphere: -lh for left, -rh for right hemisphere.
        nocerebellum: Do not process cerebellum.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "recon-all-exvivo",
        "subject_id": subject_id,
        "nocerebellum": nocerebellum,
    }
    if hemisphere is not None:
        params["hemisphere"] = hemisphere
    return params


def recon_all_exvivo_cargs(
    params: ReconAllExvivoParameters,
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
    cargs.append("recon-all-exvivo")
    cargs.extend([
        "-s",
        params.get("subject_id")
    ])
    if params.get("hemisphere") is not None:
        cargs.extend([
            "-[lr]h",
            params.get("hemisphere")
        ])
    if params.get("nocerebellum"):
        cargs.append("-nocerebellum")
    return cargs


def recon_all_exvivo_outputs(
    params: ReconAllExvivoParameters,
    execution: Execution,
) -> ReconAllExvivoOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ReconAllExvivoOutputs(
        root=execution.output_file("."),
    )
    return ret


def recon_all_exvivo_execute(
    params: ReconAllExvivoParameters,
    execution: Execution,
) -> ReconAllExvivoOutputs:
    """
    A script to perform an ex vivo reconstruction with FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ReconAllExvivoOutputs`).
    """
    params = execution.params(params)
    cargs = recon_all_exvivo_cargs(params, execution)
    ret = recon_all_exvivo_outputs(params, execution)
    execution.run(cargs)
    return ret


def recon_all_exvivo(
    subject_id: str,
    hemisphere: str | None = None,
    nocerebellum: bool = False,
    runner: Runner | None = None,
) -> ReconAllExvivoOutputs:
    """
    A script to perform an ex vivo reconstruction with FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: Subject identifier.
        hemisphere: Specify hemisphere: -lh for left, -rh for right hemisphere.
        nocerebellum: Do not process cerebellum.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReconAllExvivoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RECON_ALL_EXVIVO_METADATA)
    params = recon_all_exvivo_params(
        subject_id=subject_id,
        hemisphere=hemisphere,
        nocerebellum=nocerebellum,
    )
    return recon_all_exvivo_execute(params, execution)


__all__ = [
    "RECON_ALL_EXVIVO_METADATA",
    "ReconAllExvivoOutputs",
    "ReconAllExvivoParameters",
    "recon_all_exvivo",
    "recon_all_exvivo_params",
]
