# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

XTRACT_STATS_METADATA = Metadata(
    id="cc7ccc38ba26e6567e38306b5d134a7af2e8a430.boutiques",
    name="xtract_stats",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


XtractStatsParameters = typing.TypedDict('XtractStatsParameters', {
    "__STYX_TYPE__": typing.Literal["xtract_stats"],
    "folder_basename": str,
    "XTRACT_dir": str,
    "xtract2diff": str,
    "reference_image": typing.NotRequired[InputPathType | None],
    "output_file": typing.NotRequired[str | None],
    "structures_file": typing.NotRequired[InputPathType | None],
    "threshold": typing.NotRequired[float | None],
    "measurements": typing.NotRequired[str | None],
    "keep_temp_files": bool,
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
        "xtract_stats": xtract_stats_cargs,
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
        "xtract_stats": xtract_stats_outputs,
    }.get(t)


class XtractStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xtract_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    csv_output: OutputPathType | None
    """CSV file containing the statistics from XTRACT analysis."""


def xtract_stats_params(
    folder_basename: str,
    xtract_dir: str,
    xtract2diff: str,
    reference_image: InputPathType | None = None,
    output_file: str | None = None,
    structures_file: InputPathType | None = None,
    threshold: float | None = None,
    measurements: str | None = None,
    keep_temp_files: bool = False,
) -> XtractStatsParameters:
    """
    Build parameters.
    
    Args:
        folder_basename: Path to microstructure folder and basename of data\
            (e.g. /home/DTI/dti_).
        xtract_dir: Path to XTRACT output folder.
        xtract2diff: EITHER XTRACT results to diffusion space transform OR\
            'native' if tracts are already in diffusion space.
        reference_image: If not 'native', provide reference image in diffusion\
            space (e.g. /home/DTI/dti_FA).
        output_file: Output filepath (Default <XTRACT_dir>/stats.csv).
        structures_file: Structures file (as in XTRACT) (Default is all tracts\
            under <XTRACT_dir>).
        threshold: Threshold applied to tract probability map (default = 0.001\
            = 0.1%).
        measurements: Comma separated list of features to extract (Default =\
            vol,prob,length,FA,MD - assumes DTI folder has been provided). vol =\
            tract volume, prob = tract probability, length = tract length.\
            Additional metrics must follow file naming conventions. e.g. for dti_L1\
            use 'L1'.
        keep_temp_files: Keep temporary files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "xtract_stats",
        "folder_basename": folder_basename,
        "XTRACT_dir": xtract_dir,
        "xtract2diff": xtract2diff,
        "keep_temp_files": keep_temp_files,
    }
    if reference_image is not None:
        params["reference_image"] = reference_image
    if output_file is not None:
        params["output_file"] = output_file
    if structures_file is not None:
        params["structures_file"] = structures_file
    if threshold is not None:
        params["threshold"] = threshold
    if measurements is not None:
        params["measurements"] = measurements
    return params


def xtract_stats_cargs(
    params: XtractStatsParameters,
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
    cargs.append("xtract_stats")
    cargs.extend([
        "-d",
        params.get("folder_basename")
    ])
    cargs.extend([
        "-xtract",
        params.get("XTRACT_dir")
    ])
    cargs.extend([
        "-w",
        params.get("xtract2diff")
    ])
    if params.get("reference_image") is not None:
        cargs.extend([
            "-r",
            execution.input_file(params.get("reference_image"))
        ])
    if params.get("output_file") is not None:
        cargs.extend([
            "-out",
            params.get("output_file")
        ])
    if params.get("structures_file") is not None:
        cargs.extend([
            "-str",
            execution.input_file(params.get("structures_file"))
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "-thr",
            str(params.get("threshold"))
        ])
    if params.get("measurements") is not None:
        cargs.extend([
            "-meas",
            params.get("measurements")
        ])
    if params.get("keep_temp_files"):
        cargs.append("-keepfiles")
    return cargs


def xtract_stats_outputs(
    params: XtractStatsParameters,
    execution: Execution,
) -> XtractStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = XtractStatsOutputs(
        root=execution.output_file("."),
        csv_output=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def xtract_stats_execute(
    params: XtractStatsParameters,
    execution: Execution,
) -> XtractStatsOutputs:
    """
    Quantitative evaluation tool of XTRACT results in neuroimaging.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `XtractStatsOutputs`).
    """
    params = execution.params(params)
    cargs = xtract_stats_cargs(params, execution)
    ret = xtract_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def xtract_stats(
    folder_basename: str,
    xtract_dir: str,
    xtract2diff: str,
    reference_image: InputPathType | None = None,
    output_file: str | None = None,
    structures_file: InputPathType | None = None,
    threshold: float | None = None,
    measurements: str | None = None,
    keep_temp_files: bool = False,
    runner: Runner | None = None,
) -> XtractStatsOutputs:
    """
    Quantitative evaluation tool of XTRACT results in neuroimaging.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        folder_basename: Path to microstructure folder and basename of data\
            (e.g. /home/DTI/dti_).
        xtract_dir: Path to XTRACT output folder.
        xtract2diff: EITHER XTRACT results to diffusion space transform OR\
            'native' if tracts are already in diffusion space.
        reference_image: If not 'native', provide reference image in diffusion\
            space (e.g. /home/DTI/dti_FA).
        output_file: Output filepath (Default <XTRACT_dir>/stats.csv).
        structures_file: Structures file (as in XTRACT) (Default is all tracts\
            under <XTRACT_dir>).
        threshold: Threshold applied to tract probability map (default = 0.001\
            = 0.1%).
        measurements: Comma separated list of features to extract (Default =\
            vol,prob,length,FA,MD - assumes DTI folder has been provided). vol =\
            tract volume, prob = tract probability, length = tract length.\
            Additional metrics must follow file naming conventions. e.g. for dti_L1\
            use 'L1'.
        keep_temp_files: Keep temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XtractStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XTRACT_STATS_METADATA)
    params = xtract_stats_params(
        folder_basename=folder_basename,
        xtract_dir=xtract_dir,
        xtract2diff=xtract2diff,
        reference_image=reference_image,
        output_file=output_file,
        structures_file=structures_file,
        threshold=threshold,
        measurements=measurements,
        keep_temp_files=keep_temp_files,
    )
    return xtract_stats_execute(params, execution)


__all__ = [
    "XTRACT_STATS_METADATA",
    "XtractStatsOutputs",
    "XtractStatsParameters",
    "xtract_stats",
    "xtract_stats_params",
]
