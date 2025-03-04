# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

XCEREBRALSEG_METADATA = Metadata(
    id="14c3690bac7554084d7978a923e6d146bea56460.boutiques",
    name="xcerebralseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


XcerebralsegParameters = typing.TypedDict('XcerebralsegParameters', {
    "__STYX_TYPE__": typing.Literal["xcerebralseg"],
    "subject": str,
    "output_volume": typing.NotRequired[str | None],
    "atlas": typing.NotRequired[str | None],
    "mergevol": typing.NotRequired[str | None],
    "source_volume": typing.NotRequired[str | None],
    "no_stats": bool,
    "seg1_name": typing.NotRequired[str | None],
    "no_pons": bool,
    "no_vermis": bool,
    "threads": typing.NotRequired[float | None],
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
        "xcerebralseg": xcerebralseg_cargs,
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
        "xcerebralseg": xcerebralseg_outputs,
    }.get(t)


class XcerebralsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xcerebralseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Output volume file for the whole head segmentation"""


def xcerebralseg_params(
    subject: str,
    output_volume: str | None = "apas+head.mgz",
    atlas: str | None = "/usr/local/freesurfer/average/aseg+spmhead+vermis+pons.ixi.gca",
    mergevol: str | None = "aparc+aseg.mgz",
    source_volume: str | None = "nu.mgz",
    no_stats: bool = False,
    seg1_name: str | None = None,
    no_pons: bool = False,
    no_vermis: bool = False,
    threads: float | None = None,
) -> XcerebralsegParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier (required).
        output_volume: Output volume file (default: apas+head.mgz).
        atlas: Atlas file path (default:\
            /usr/local/freesurfer/average/aseg+spmhead+vermis+pons.ixi.gca).
        mergevol: Merge with mergevol (default: aparc+aseg.mgz).
        source_volume: Source intensity volume (default: nu.mgz).
        no_stats: Do not run mri_segstats.
        seg1_name: Full-head segmentation name (usually computed with\
            mri_ca_label).
        no_pons: Exclude pons segmentation.
        no_vermis: Exclude vermis segmentation.
        threads: Set number of OPENMP threads.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "xcerebralseg",
        "subject": subject,
        "no_stats": no_stats,
        "no_pons": no_pons,
        "no_vermis": no_vermis,
    }
    if output_volume is not None:
        params["output_volume"] = output_volume
    if atlas is not None:
        params["atlas"] = atlas
    if mergevol is not None:
        params["mergevol"] = mergevol
    if source_volume is not None:
        params["source_volume"] = source_volume
    if seg1_name is not None:
        params["seg1_name"] = seg1_name
    if threads is not None:
        params["threads"] = threads
    return params


def xcerebralseg_cargs(
    params: XcerebralsegParameters,
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
    cargs.append("xcerebralseg")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("output_volume") is not None:
        cargs.extend([
            "--o",
            params.get("output_volume")
        ])
    if params.get("atlas") is not None:
        cargs.extend([
            "--atlas",
            params.get("atlas")
        ])
    if params.get("mergevol") is not None:
        cargs.extend([
            "--m",
            params.get("mergevol")
        ])
    if params.get("source_volume") is not None:
        cargs.extend([
            "--srcvol",
            params.get("source_volume")
        ])
    if params.get("no_stats"):
        cargs.append("--no-stats")
    if params.get("seg1_name") is not None:
        cargs.extend([
            "--seg1",
            params.get("seg1_name")
        ])
    if params.get("no_pons"):
        cargs.append("--no-pons")
    if params.get("no_vermis"):
        cargs.append("--no-vermis")
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    return cargs


def xcerebralseg_outputs(
    params: XcerebralsegParameters,
    execution: Execution,
) -> XcerebralsegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = XcerebralsegOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file("apas+head.mgz"),
    )
    return ret


def xcerebralseg_execute(
    params: XcerebralsegParameters,
    execution: Execution,
) -> XcerebralsegOutputs:
    """
    Tool for labeling extracerebral structures including sulcal CSF, skull/bone,
    head soft tissue, and air inside the head, merged with aparc+aseg.mgz
    segmentation for a whole head segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `XcerebralsegOutputs`).
    """
    params = execution.params(params)
    cargs = xcerebralseg_cargs(params, execution)
    ret = xcerebralseg_outputs(params, execution)
    execution.run(cargs)
    return ret


def xcerebralseg(
    subject: str,
    output_volume: str | None = "apas+head.mgz",
    atlas: str | None = "/usr/local/freesurfer/average/aseg+spmhead+vermis+pons.ixi.gca",
    mergevol: str | None = "aparc+aseg.mgz",
    source_volume: str | None = "nu.mgz",
    no_stats: bool = False,
    seg1_name: str | None = None,
    no_pons: bool = False,
    no_vermis: bool = False,
    threads: float | None = None,
    runner: Runner | None = None,
) -> XcerebralsegOutputs:
    """
    Tool for labeling extracerebral structures including sulcal CSF, skull/bone,
    head soft tissue, and air inside the head, merged with aparc+aseg.mgz
    segmentation for a whole head segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier (required).
        output_volume: Output volume file (default: apas+head.mgz).
        atlas: Atlas file path (default:\
            /usr/local/freesurfer/average/aseg+spmhead+vermis+pons.ixi.gca).
        mergevol: Merge with mergevol (default: aparc+aseg.mgz).
        source_volume: Source intensity volume (default: nu.mgz).
        no_stats: Do not run mri_segstats.
        seg1_name: Full-head segmentation name (usually computed with\
            mri_ca_label).
        no_pons: Exclude pons segmentation.
        no_vermis: Exclude vermis segmentation.
        threads: Set number of OPENMP threads.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XcerebralsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XCEREBRALSEG_METADATA)
    params = xcerebralseg_params(
        subject=subject,
        output_volume=output_volume,
        atlas=atlas,
        mergevol=mergevol,
        source_volume=source_volume,
        no_stats=no_stats,
        seg1_name=seg1_name,
        no_pons=no_pons,
        no_vermis=no_vermis,
        threads=threads,
    )
    return xcerebralseg_execute(params, execution)


__all__ = [
    "XCEREBRALSEG_METADATA",
    "XcerebralsegOutputs",
    "XcerebralsegParameters",
    "xcerebralseg",
    "xcerebralseg_params",
]
