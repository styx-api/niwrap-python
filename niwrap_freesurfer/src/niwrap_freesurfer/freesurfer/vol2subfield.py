# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOL2SUBFIELD_METADATA = Metadata(
    id="691e0cc8560feeb387d8f3217fe9bed3e94cc38e.boutiques",
    name="vol2subfield",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Vol2subfieldParameters = typing.TypedDict('Vol2subfieldParameters', {
    "__STYX_TYPE__": typing.Literal["vol2subfield"],
    "input_volume": InputPathType,
    "subfield_volume": InputPathType,
    "registration_file": InputPathType,
    "output_volume": typing.NotRequired[str | None],
    "output_registration": typing.NotRequired[str | None],
    "stats_output": typing.NotRequired[str | None],
    "avgwf_output": typing.NotRequired[str | None],
    "avgwfvol_output": typing.NotRequired[str | None],
    "color_table": typing.NotRequired[InputPathType | None],
    "interpolation_nearest": bool,
    "interpolation_trilin": bool,
    "interpolation_cubic": bool,
    "tmp_directory": typing.NotRequired[str | None],
    "preset_subfield_lh_hippoamyg": bool,
    "preset_subfield_rh_hippoamyg": bool,
    "preset_subfield_lh_hbt": bool,
    "preset_subfield_rh_hbt": bool,
    "preset_subfield_thalamus": bool,
    "preset_subfield_brainstem": bool,
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
        "vol2subfield": vol2subfield_cargs,
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
        "vol2subfield": vol2subfield_outputs,
    }.get(t)


class Vol2subfieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `vol2subfield(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mapped_output_volume: OutputPathType | None
    """Output volume mapped into subfield volume space"""
    output_registration_file: OutputPathType | None
    """Output registration file"""
    segmentation_stats_file: OutputPathType | None
    """Statistics output file generated by mri_segstats"""
    average_waveform_file: OutputPathType | None
    """Average waveform output file"""
    average_waveform_volume_file: OutputPathType | None
    """Average waveform volume output file"""


def vol2subfield_params(
    input_volume: InputPathType,
    subfield_volume: InputPathType,
    registration_file: InputPathType,
    output_volume: str | None = None,
    output_registration: str | None = None,
    stats_output: str | None = None,
    avgwf_output: str | None = None,
    avgwfvol_output: str | None = None,
    color_table: InputPathType | None = None,
    interpolation_nearest: bool = False,
    interpolation_trilin: bool = False,
    interpolation_cubic: bool = False,
    tmp_directory: str | None = None,
    preset_subfield_lh_hippoamyg: bool = False,
    preset_subfield_rh_hippoamyg: bool = False,
    preset_subfield_lh_hbt: bool = False,
    preset_subfield_rh_hbt: bool = False,
    preset_subfield_thalamus: bool = False,
    preset_subfield_brainstem: bool = False,
) -> Vol2subfieldParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume.
        subfield_volume: Subfield volume (full path or relative to subject/mri).
        registration_file: Registration that maps input volume to conformed\
            space.
        output_volume: Output volume.
        output_registration: Registration between input volume and subfield.
        stats_output: Run mri_segstats with --sum output to this file.
        avgwf_output: Run mri_segstats with --avgwf output to this file.
        avgwfvol_output: Run mri_segstats with --avgwfvol output to this file.
        color_table: Color table to use with mri_segstats.
        interpolation_nearest: Use nearest neighbor interpolation.
        interpolation_trilin: Use triliear interpolation.
        interpolation_cubic: Use cubic interpolation.
        tmp_directory: Temporary directory for debugging.
        preset_subfield_lh_hippoamyg: Set subfield to\
            lh.hippoAmygLabels-T1.v21.mgz.
        preset_subfield_rh_hippoamyg: Set subfield to\
            rh.hippoAmygLabels-T1.v21.mgz.
        preset_subfield_lh_hbt: Set subfield to\
            lh.hippoAmygLabels-T1.v21.HBT.mgz.
        preset_subfield_rh_hbt: Set subfield to\
            rh.hippoAmygLabels-T1.v21.HBT.mgz.
        preset_subfield_thalamus: Set subfield to ThalamicNuclei.v10.T1.mgz.
        preset_subfield_brainstem: Set subfield to brainstemSsLabels.v12.mgz.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "vol2subfield",
        "input_volume": input_volume,
        "subfield_volume": subfield_volume,
        "registration_file": registration_file,
        "interpolation_nearest": interpolation_nearest,
        "interpolation_trilin": interpolation_trilin,
        "interpolation_cubic": interpolation_cubic,
        "preset_subfield_lh_hippoamyg": preset_subfield_lh_hippoamyg,
        "preset_subfield_rh_hippoamyg": preset_subfield_rh_hippoamyg,
        "preset_subfield_lh_hbt": preset_subfield_lh_hbt,
        "preset_subfield_rh_hbt": preset_subfield_rh_hbt,
        "preset_subfield_thalamus": preset_subfield_thalamus,
        "preset_subfield_brainstem": preset_subfield_brainstem,
    }
    if output_volume is not None:
        params["output_volume"] = output_volume
    if output_registration is not None:
        params["output_registration"] = output_registration
    if stats_output is not None:
        params["stats_output"] = stats_output
    if avgwf_output is not None:
        params["avgwf_output"] = avgwf_output
    if avgwfvol_output is not None:
        params["avgwfvol_output"] = avgwfvol_output
    if color_table is not None:
        params["color_table"] = color_table
    if tmp_directory is not None:
        params["tmp_directory"] = tmp_directory
    return params


def vol2subfield_cargs(
    params: Vol2subfieldParameters,
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
    cargs.append("vol2subfield")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "--sf",
        execution.input_file(params.get("subfield_volume"))
    ])
    cargs.extend([
        "--reg",
        execution.input_file(params.get("registration_file"))
    ])
    if params.get("output_volume") is not None:
        cargs.extend([
            "--o",
            params.get("output_volume")
        ])
    if params.get("output_registration") is not None:
        cargs.extend([
            "--outreg",
            params.get("output_registration")
        ])
    if params.get("stats_output") is not None:
        cargs.extend([
            "--stats",
            params.get("stats_output")
        ])
    if params.get("avgwf_output") is not None:
        cargs.extend([
            "--avgwf",
            params.get("avgwf_output")
        ])
    if params.get("avgwfvol_output") is not None:
        cargs.extend([
            "--avgwfvol",
            params.get("avgwfvol_output")
        ])
    if params.get("color_table") is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(params.get("color_table"))
        ])
    if params.get("interpolation_nearest"):
        cargs.append("--nearest")
    if params.get("interpolation_trilin"):
        cargs.append("--trilin")
    if params.get("interpolation_cubic"):
        cargs.append("--cubic")
    if params.get("tmp_directory") is not None:
        cargs.extend([
            "--tmp",
            params.get("tmp_directory")
        ])
    if params.get("preset_subfield_lh_hippoamyg"):
        cargs.append("--lh.hippoamyg")
    if params.get("preset_subfield_rh_hippoamyg"):
        cargs.append("--rh.hippoamyg")
    if params.get("preset_subfield_lh_hbt"):
        cargs.append("--lh.hbt")
    if params.get("preset_subfield_rh_hbt"):
        cargs.append("--rh.hbt")
    if params.get("preset_subfield_thalamus"):
        cargs.append("--thalamus")
    if params.get("preset_subfield_brainstem"):
        cargs.append("--brainstem")
    return cargs


def vol2subfield_outputs(
    params: Vol2subfieldParameters,
    execution: Execution,
) -> Vol2subfieldOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Vol2subfieldOutputs(
        root=execution.output_file("."),
        mapped_output_volume=execution.output_file(params.get("output_volume")) if (params.get("output_volume") is not None) else None,
        output_registration_file=execution.output_file(params.get("output_registration")) if (params.get("output_registration") is not None) else None,
        segmentation_stats_file=execution.output_file(params.get("stats_output")) if (params.get("stats_output") is not None) else None,
        average_waveform_file=execution.output_file(params.get("avgwf_output")) if (params.get("avgwf_output") is not None) else None,
        average_waveform_volume_file=execution.output_file(params.get("avgwfvol_output")) if (params.get("avgwfvol_output") is not None) else None,
    )
    return ret


def vol2subfield_execute(
    params: Vol2subfieldParameters,
    execution: Execution,
) -> Vol2subfieldOutputs:
    """
    A tool for integrating arbitrary volumes with volumes that share a RAS space
    with the orig volume in the FreeSurfer mri folder.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Vol2subfieldOutputs`).
    """
    params = execution.params(params)
    cargs = vol2subfield_cargs(params, execution)
    ret = vol2subfield_outputs(params, execution)
    execution.run(cargs)
    return ret


def vol2subfield(
    input_volume: InputPathType,
    subfield_volume: InputPathType,
    registration_file: InputPathType,
    output_volume: str | None = None,
    output_registration: str | None = None,
    stats_output: str | None = None,
    avgwf_output: str | None = None,
    avgwfvol_output: str | None = None,
    color_table: InputPathType | None = None,
    interpolation_nearest: bool = False,
    interpolation_trilin: bool = False,
    interpolation_cubic: bool = False,
    tmp_directory: str | None = None,
    preset_subfield_lh_hippoamyg: bool = False,
    preset_subfield_rh_hippoamyg: bool = False,
    preset_subfield_lh_hbt: bool = False,
    preset_subfield_rh_hbt: bool = False,
    preset_subfield_thalamus: bool = False,
    preset_subfield_brainstem: bool = False,
    runner: Runner | None = None,
) -> Vol2subfieldOutputs:
    """
    A tool for integrating arbitrary volumes with volumes that share a RAS space
    with the orig volume in the FreeSurfer mri folder.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume.
        subfield_volume: Subfield volume (full path or relative to subject/mri).
        registration_file: Registration that maps input volume to conformed\
            space.
        output_volume: Output volume.
        output_registration: Registration between input volume and subfield.
        stats_output: Run mri_segstats with --sum output to this file.
        avgwf_output: Run mri_segstats with --avgwf output to this file.
        avgwfvol_output: Run mri_segstats with --avgwfvol output to this file.
        color_table: Color table to use with mri_segstats.
        interpolation_nearest: Use nearest neighbor interpolation.
        interpolation_trilin: Use triliear interpolation.
        interpolation_cubic: Use cubic interpolation.
        tmp_directory: Temporary directory for debugging.
        preset_subfield_lh_hippoamyg: Set subfield to\
            lh.hippoAmygLabels-T1.v21.mgz.
        preset_subfield_rh_hippoamyg: Set subfield to\
            rh.hippoAmygLabels-T1.v21.mgz.
        preset_subfield_lh_hbt: Set subfield to\
            lh.hippoAmygLabels-T1.v21.HBT.mgz.
        preset_subfield_rh_hbt: Set subfield to\
            rh.hippoAmygLabels-T1.v21.HBT.mgz.
        preset_subfield_thalamus: Set subfield to ThalamicNuclei.v10.T1.mgz.
        preset_subfield_brainstem: Set subfield to brainstemSsLabels.v12.mgz.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Vol2subfieldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOL2SUBFIELD_METADATA)
    params = vol2subfield_params(
        input_volume=input_volume,
        subfield_volume=subfield_volume,
        registration_file=registration_file,
        output_volume=output_volume,
        output_registration=output_registration,
        stats_output=stats_output,
        avgwf_output=avgwf_output,
        avgwfvol_output=avgwfvol_output,
        color_table=color_table,
        interpolation_nearest=interpolation_nearest,
        interpolation_trilin=interpolation_trilin,
        interpolation_cubic=interpolation_cubic,
        tmp_directory=tmp_directory,
        preset_subfield_lh_hippoamyg=preset_subfield_lh_hippoamyg,
        preset_subfield_rh_hippoamyg=preset_subfield_rh_hippoamyg,
        preset_subfield_lh_hbt=preset_subfield_lh_hbt,
        preset_subfield_rh_hbt=preset_subfield_rh_hbt,
        preset_subfield_thalamus=preset_subfield_thalamus,
        preset_subfield_brainstem=preset_subfield_brainstem,
    )
    return vol2subfield_execute(params, execution)


__all__ = [
    "VOL2SUBFIELD_METADATA",
    "Vol2subfieldOutputs",
    "Vol2subfieldParameters",
    "vol2subfield",
    "vol2subfield_params",
]
