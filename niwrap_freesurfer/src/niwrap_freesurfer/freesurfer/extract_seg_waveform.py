# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

EXTRACT_SEG_WAVEFORM_METADATA = Metadata(
    id="1e8d726c7b2975eda55d107c6a157a6568cc1f02.boutiques",
    name="extract_seg_waveform",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


ExtractSegWaveformParameters = typing.TypedDict('ExtractSegWaveformParameters', {
    "__STYX_TYPE__": typing.Literal["extract_seg_waveform"],
    "seg_file": InputPathType,
    "seg_indices": list[float],
    "input_volume": InputPathType,
    "reg_file": InputPathType,
    "vsm_file": typing.NotRequired[InputPathType | None],
    "regheader_flag": bool,
    "demean_flag": bool,
    "output_file": str,
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
        "extract_seg_waveform": extract_seg_waveform_cargs,
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


class ExtractSegWaveformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `extract_seg_waveform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def extract_seg_waveform_params(
    seg_file: InputPathType,
    seg_indices: list[float],
    input_volume: InputPathType,
    reg_file: InputPathType,
    output_file: str,
    vsm_file: InputPathType | None = None,
    regheader_flag: bool = False,
    demean_flag: bool = False,
) -> ExtractSegWaveformParameters:
    """
    Build parameters.
    
    Args:
        seg_file: Segmentation file.
        seg_indices: Segmentation indices, one or more indices can be specified.
        input_volume: Input volume.
        reg_file: Registration file (.lta).
        output_file: Output waveform file.
        vsm_file: Voxel shift map for B0 distortion correction.
        regheader_flag: Uses the header information in the registration file.
        demean_flag: Remove mean, first, and second order trends.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "extract_seg_waveform",
        "seg_file": seg_file,
        "seg_indices": seg_indices,
        "input_volume": input_volume,
        "reg_file": reg_file,
        "regheader_flag": regheader_flag,
        "demean_flag": demean_flag,
        "output_file": output_file,
    }
    if vsm_file is not None:
        params["vsm_file"] = vsm_file
    return params


def extract_seg_waveform_cargs(
    params: ExtractSegWaveformParameters,
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
    cargs.append("extract_seg_waveform")
    cargs.extend([
        "--seg",
        execution.input_file(params.get("seg_file"))
    ])
    cargs.extend([
        "--id",
        *map(str, params.get("seg_indices"))
    ])
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "--reg",
        execution.input_file(params.get("reg_file"))
    ])
    if params.get("vsm_file") is not None:
        cargs.extend([
            "--vsm",
            execution.input_file(params.get("vsm_file"))
        ])
    if params.get("regheader_flag"):
        cargs.append("--regheader")
    if params.get("demean_flag"):
        cargs.append("--demean")
    cargs.extend([
        "--o",
        params.get("output_file")
    ])
    return cargs


def extract_seg_waveform_outputs(
    params: ExtractSegWaveformParameters,
    execution: Execution,
) -> ExtractSegWaveformOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ExtractSegWaveformOutputs(
        root=execution.output_file("."),
    )
    return ret


def extract_seg_waveform_execute(
    params: ExtractSegWaveformParameters,
    execution: Execution,
) -> ExtractSegWaveformOutputs:
    """
    This program extracts an average waveform from an input volume where the average
    is computed over the voxels in the given segmentation indices. The input volume
    is mapped to the space of the segmentation given the registration, and if a
    voxel shift map (VSM) is supplied, it is applied simultaneously as part of the
    transform.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ExtractSegWaveformOutputs`).
    """
    params = execution.params(params)
    cargs = extract_seg_waveform_cargs(params, execution)
    ret = extract_seg_waveform_outputs(params, execution)
    execution.run(cargs)
    return ret


def extract_seg_waveform(
    seg_file: InputPathType,
    seg_indices: list[float],
    input_volume: InputPathType,
    reg_file: InputPathType,
    output_file: str,
    vsm_file: InputPathType | None = None,
    regheader_flag: bool = False,
    demean_flag: bool = False,
    runner: Runner | None = None,
) -> ExtractSegWaveformOutputs:
    """
    This program extracts an average waveform from an input volume where the average
    is computed over the voxels in the given segmentation indices. The input volume
    is mapped to the space of the segmentation given the registration, and if a
    voxel shift map (VSM) is supplied, it is applied simultaneously as part of the
    transform.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        seg_file: Segmentation file.
        seg_indices: Segmentation indices, one or more indices can be specified.
        input_volume: Input volume.
        reg_file: Registration file (.lta).
        output_file: Output waveform file.
        vsm_file: Voxel shift map for B0 distortion correction.
        regheader_flag: Uses the header information in the registration file.
        demean_flag: Remove mean, first, and second order trends.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ExtractSegWaveformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EXTRACT_SEG_WAVEFORM_METADATA)
    params = extract_seg_waveform_params(
        seg_file=seg_file,
        seg_indices=seg_indices,
        input_volume=input_volume,
        reg_file=reg_file,
        vsm_file=vsm_file,
        regheader_flag=regheader_flag,
        demean_flag=demean_flag,
        output_file=output_file,
    )
    return extract_seg_waveform_execute(params, execution)


__all__ = [
    "EXTRACT_SEG_WAVEFORM_METADATA",
    "ExtractSegWaveformOutputs",
    "ExtractSegWaveformParameters",
    "extract_seg_waveform",
    "extract_seg_waveform_params",
]
