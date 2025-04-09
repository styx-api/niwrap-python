# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

WM_ANAT_SNR_METADATA = Metadata(
    id="720d73c797ea6b11df6f56d663b8a31bbc7866b2.boutiques",
    name="wm-anat-snr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


WmAnatSnrParameters = typing.TypedDict('WmAnatSnrParameters', {
    "__STYX_TYPE__": typing.Literal["wm-anat-snr"],
    "subject": str,
    "output_file": str,
    "force": bool,
    "nerode": typing.NotRequired[int | None],
    "tmp_dir": typing.NotRequired[str | None],
    "cleanup": bool,
    "no_cleanup": bool,
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
        "wm-anat-snr": wm_anat_snr_cargs,
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
        "wm-anat-snr": wm_anat_snr_outputs,
    }.get(t)


class WmAnatSnrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `wm_anat_snr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_datafile: OutputPathType
    """Output data file containing SNR and associated metrics"""


def wm_anat_snr_params(
    subject: str,
    output_file: str,
    force: bool = False,
    nerode: int | None = None,
    tmp_dir: str | None = None,
    cleanup: bool = False,
    no_cleanup: bool = False,
) -> WmAnatSnrParameters:
    """
    Build parameters.
    
    Args:
        subject: FreeSurfer subject name.
        output_file: Output file.
        force: Force analysis even if output is up-to-date.
        nerode: Number of erosions for the WM mask.
        tmp_dir: Temporary directory.
        cleanup: Delete temporary directory after execution.
        no_cleanup: Do not delete temporary directory after execution.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "wm-anat-snr",
        "subject": subject,
        "output_file": output_file,
        "force": force,
        "cleanup": cleanup,
        "no_cleanup": no_cleanup,
    }
    if nerode is not None:
        params["nerode"] = nerode
    if tmp_dir is not None:
        params["tmp_dir"] = tmp_dir
    return params


def wm_anat_snr_cargs(
    params: WmAnatSnrParameters,
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
    cargs.append("wm-anat-snr")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    cargs.extend([
        "--o",
        params.get("output_file")
    ])
    if params.get("force"):
        cargs.append("--force")
    if params.get("nerode") is not None:
        cargs.extend([
            "--nerode",
            str(params.get("nerode"))
        ])
    if params.get("tmp_dir") is not None:
        cargs.extend([
            "--tmp",
            params.get("tmp_dir")
        ])
    if params.get("cleanup"):
        cargs.append("--cleanup")
    if params.get("no_cleanup"):
        cargs.append("--no-cleanup")
    return cargs


def wm_anat_snr_outputs(
    params: WmAnatSnrParameters,
    execution: Execution,
) -> WmAnatSnrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = WmAnatSnrOutputs(
        root=execution.output_file("."),
        output_datafile=execution.output_file(params.get("output_file")),
    )
    return ret


def wm_anat_snr_execute(
    params: WmAnatSnrParameters,
    execution: Execution,
) -> WmAnatSnrOutputs:
    """
    Measures the anatomical SNR in white matter (WM) for quality assurance (QA).
    This is an experimental metric.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `WmAnatSnrOutputs`).
    """
    params = execution.params(params)
    cargs = wm_anat_snr_cargs(params, execution)
    ret = wm_anat_snr_outputs(params, execution)
    execution.run(cargs)
    return ret


def wm_anat_snr(
    subject: str,
    output_file: str,
    force: bool = False,
    nerode: int | None = None,
    tmp_dir: str | None = None,
    cleanup: bool = False,
    no_cleanup: bool = False,
    runner: Runner | None = None,
) -> WmAnatSnrOutputs:
    """
    Measures the anatomical SNR in white matter (WM) for quality assurance (QA).
    This is an experimental metric.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: FreeSurfer subject name.
        output_file: Output file.
        force: Force analysis even if output is up-to-date.
        nerode: Number of erosions for the WM mask.
        tmp_dir: Temporary directory.
        cleanup: Delete temporary directory after execution.
        no_cleanup: Do not delete temporary directory after execution.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WmAnatSnrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WM_ANAT_SNR_METADATA)
    params = wm_anat_snr_params(
        subject=subject,
        output_file=output_file,
        force=force,
        nerode=nerode,
        tmp_dir=tmp_dir,
        cleanup=cleanup,
        no_cleanup=no_cleanup,
    )
    return wm_anat_snr_execute(params, execution)


__all__ = [
    "WM_ANAT_SNR_METADATA",
    "WmAnatSnrOutputs",
    "WmAnatSnrParameters",
    "wm_anat_snr",
    "wm_anat_snr_params",
]
