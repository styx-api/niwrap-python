# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PRELUDE_METADATA = Metadata(
    id="dccfbfdb8ed4e23f2a95b3d7d1951fe254df6693.boutiques",
    name="prelude",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


PreludeParameters = typing.TypedDict('PreludeParameters', {
    "__STYXTYPE__": typing.Literal["prelude"],
    "output_unwrap": str,
    "output_unwrap_alias": InputPathType,
    "complex_phase": typing.NotRequired[InputPathType | None],
    "complex_phase_alias": typing.NotRequired[InputPathType | None],
    "absolute_volume": typing.NotRequired[InputPathType | None],
    "absolute_volume_alias": typing.NotRequired[InputPathType | None],
    "phase_volume": typing.NotRequired[InputPathType | None],
    "phase_volume_alias": typing.NotRequired[InputPathType | None],
    "num_phase_split": typing.NotRequired[float | None],
    "label_slices": bool,
    "slice_processing": bool,
    "slice_processing_alias": bool,
    "force_3d": bool,
    "force_3d_alias": bool,
    "threshold": typing.NotRequired[float | None],
    "threshold_alias": typing.NotRequired[float | None],
    "mask_volume": typing.NotRequired[InputPathType | None],
    "mask_volume_alias": typing.NotRequired[InputPathType | None],
    "start_image": typing.NotRequired[float | None],
    "end_image": typing.NotRequired[float | None],
    "save_mask": typing.NotRequired[InputPathType | None],
    "save_raw_phase": typing.NotRequired[InputPathType | None],
    "save_raw_phase_alias": typing.NotRequired[InputPathType | None],
    "save_labels": typing.NotRequired[InputPathType | None],
    "save_labels_alias": typing.NotRequired[InputPathType | None],
    "remove_ramps": bool,
    "verbose": bool,
    "verbose_alias": bool,
    "help": bool,
    "help_alias": bool,
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
        "prelude": prelude_cargs,
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
        "prelude": prelude_outputs,
    }.get(t)


class PreludeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `prelude(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    unwrapped_phase_output: OutputPathType
    """Unwrapped phase output file"""
    saved_mask_volume: OutputPathType | None
    """Saved mask volume file"""
    saved_raw_phase_output: OutputPathType | None
    """Saved raw phase output file"""
    saved_area_labels_output: OutputPathType | None
    """Saved area labels output file"""


def prelude_params(
    output_unwrap: str,
    output_unwrap_alias: InputPathType,
    complex_phase: InputPathType | None = None,
    complex_phase_alias: InputPathType | None = None,
    absolute_volume: InputPathType | None = None,
    absolute_volume_alias: InputPathType | None = None,
    phase_volume: InputPathType | None = None,
    phase_volume_alias: InputPathType | None = None,
    num_phase_split: float | None = None,
    label_slices: bool = False,
    slice_processing: bool = False,
    slice_processing_alias: bool = False,
    force_3d: bool = False,
    force_3d_alias: bool = False,
    threshold: float | None = None,
    threshold_alias: float | None = None,
    mask_volume: InputPathType | None = None,
    mask_volume_alias: InputPathType | None = None,
    start_image: float | None = None,
    end_image: float | None = None,
    save_mask: InputPathType | None = None,
    save_raw_phase: InputPathType | None = None,
    save_raw_phase_alias: InputPathType | None = None,
    save_labels: InputPathType | None = None,
    save_labels_alias: InputPathType | None = None,
    remove_ramps: bool = False,
    verbose: bool = False,
    verbose_alias: bool = False,
    help_: bool = False,
    help_alias: bool = False,
) -> PreludeParameters:
    """
    Build parameters.
    
    Args:
        output_unwrap: Filename for saving the unwrapped phase output.
        output_unwrap_alias: Filename for saving the unwrapped phase output.
        complex_phase: Filename of complex phase input volume.
        complex_phase_alias: Filename of complex phase input volume.
        absolute_volume: Filename of absolute input volume.
        absolute_volume_alias: Filename of absolute input volume.
        phase_volume: Filename of raw phase input volume.
        phase_volume_alias: Filename of raw phase input volume.
        num_phase_split: Number of phase partitions to use.
        label_slices: Does label processing in 2D (slice at a time).
        slice_processing: Does all processing in 2D (slice at a time).
        slice_processing_alias: Does all processing in 2D (slice at a time).
        force_3d: Forces all processing to be full 3D.
        force_3d_alias: Forces all processing to be full 3D.
        threshold: Intensity threshold for masking.
        threshold_alias: Intensity threshold for masking.
        mask_volume: Filename of mask input volume.
        mask_volume_alias: Filename of mask input volume.
        start_image: First image number to process (default 0).
        end_image: Final image number to process (default Inf).
        save_mask: Filename for saving the mask volume.
        save_raw_phase: Filename for saving the raw phase output.
        save_raw_phase_alias: Filename for saving the raw phase output.
        save_labels: Filename for saving the area labels output.
        save_labels_alias: Filename for saving the area labels output.
        remove_ramps: Remove phase ramps during unwrapping.
        verbose: Switch on diagnostic messages.
        verbose_alias: Switch on diagnostic messages.
        help_: Display help message.
        help_alias: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "prelude",
        "output_unwrap": output_unwrap,
        "output_unwrap_alias": output_unwrap_alias,
        "label_slices": label_slices,
        "slice_processing": slice_processing,
        "slice_processing_alias": slice_processing_alias,
        "force_3d": force_3d,
        "force_3d_alias": force_3d_alias,
        "remove_ramps": remove_ramps,
        "verbose": verbose,
        "verbose_alias": verbose_alias,
        "help": help_,
        "help_alias": help_alias,
    }
    if complex_phase is not None:
        params["complex_phase"] = complex_phase
    if complex_phase_alias is not None:
        params["complex_phase_alias"] = complex_phase_alias
    if absolute_volume is not None:
        params["absolute_volume"] = absolute_volume
    if absolute_volume_alias is not None:
        params["absolute_volume_alias"] = absolute_volume_alias
    if phase_volume is not None:
        params["phase_volume"] = phase_volume
    if phase_volume_alias is not None:
        params["phase_volume_alias"] = phase_volume_alias
    if num_phase_split is not None:
        params["num_phase_split"] = num_phase_split
    if threshold is not None:
        params["threshold"] = threshold
    if threshold_alias is not None:
        params["threshold_alias"] = threshold_alias
    if mask_volume is not None:
        params["mask_volume"] = mask_volume
    if mask_volume_alias is not None:
        params["mask_volume_alias"] = mask_volume_alias
    if start_image is not None:
        params["start_image"] = start_image
    if end_image is not None:
        params["end_image"] = end_image
    if save_mask is not None:
        params["save_mask"] = save_mask
    if save_raw_phase is not None:
        params["save_raw_phase"] = save_raw_phase
    if save_raw_phase_alias is not None:
        params["save_raw_phase_alias"] = save_raw_phase_alias
    if save_labels is not None:
        params["save_labels"] = save_labels
    if save_labels_alias is not None:
        params["save_labels_alias"] = save_labels_alias
    return params


def prelude_cargs(
    params: PreludeParameters,
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
    cargs.append("prelude")
    cargs.extend([
        "-o",
        params.get("output_unwrap")
    ])
    cargs.extend([
        "-u",
        execution.input_file(params.get("output_unwrap_alias"))
    ])
    if params.get("complex_phase") is not None:
        cargs.extend([
            "-c",
            execution.input_file(params.get("complex_phase"))
        ])
    if params.get("complex_phase_alias") is not None:
        cargs.extend([
            "--complex",
            execution.input_file(params.get("complex_phase_alias"))
        ])
    if params.get("absolute_volume") is not None:
        cargs.extend([
            "-a",
            execution.input_file(params.get("absolute_volume"))
        ])
    if params.get("absolute_volume_alias") is not None:
        cargs.extend([
            "--abs",
            execution.input_file(params.get("absolute_volume_alias"))
        ])
    if params.get("phase_volume") is not None:
        cargs.extend([
            "-p",
            execution.input_file(params.get("phase_volume"))
        ])
    if params.get("phase_volume_alias") is not None:
        cargs.extend([
            "--phase",
            execution.input_file(params.get("phase_volume_alias"))
        ])
    if params.get("num_phase_split") is not None:
        cargs.extend([
            "-n",
            str(params.get("num_phase_split"))
        ])
    if params.get("label_slices"):
        cargs.append("--labelslices")
    if params.get("slice_processing"):
        cargs.append("-s")
    if params.get("slice_processing_alias"):
        cargs.append("--slices")
    if params.get("force_3d"):
        cargs.append("-f")
    if params.get("force_3d_alias"):
        cargs.append("--force3D")
    if params.get("threshold") is not None:
        cargs.extend([
            "-t",
            str(params.get("threshold"))
        ])
    if params.get("threshold_alias") is not None:
        cargs.extend([
            "--thresh",
            str(params.get("threshold_alias"))
        ])
    if params.get("mask_volume") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask_volume"))
        ])
    if params.get("mask_volume_alias") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask_volume_alias"))
        ])
    if params.get("start_image") is not None:
        cargs.extend([
            "--start",
            str(params.get("start_image"))
        ])
    if params.get("end_image") is not None:
        cargs.extend([
            "--end",
            str(params.get("end_image"))
        ])
    if params.get("save_mask") is not None:
        cargs.extend([
            "--savemask",
            execution.input_file(params.get("save_mask"))
        ])
    if params.get("save_raw_phase") is not None:
        cargs.extend([
            "-r",
            execution.input_file(params.get("save_raw_phase"))
        ])
    if params.get("save_raw_phase_alias") is not None:
        cargs.extend([
            "--rawphase",
            execution.input_file(params.get("save_raw_phase_alias"))
        ])
    if params.get("save_labels") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("save_labels"))
        ])
    if params.get("save_labels_alias") is not None:
        cargs.extend([
            "--labels",
            execution.input_file(params.get("save_labels_alias"))
        ])
    if params.get("remove_ramps"):
        cargs.append("--removeramps")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("verbose_alias"):
        cargs.append("--verbose")
    if params.get("help"):
        cargs.append("-h")
    if params.get("help_alias"):
        cargs.append("--help")
    return cargs


def prelude_outputs(
    params: PreludeParameters,
    execution: Execution,
) -> PreludeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PreludeOutputs(
        root=execution.output_file("."),
        unwrapped_phase_output=execution.output_file(params.get("output_unwrap") + ".nii.gz"),
        saved_mask_volume=execution.output_file(pathlib.Path(params.get("save_mask")).name + ".nii.gz") if (params.get("save_mask") is not None) else None,
        saved_raw_phase_output=execution.output_file(pathlib.Path(params.get("save_raw_phase")).name + ".nii.gz") if (params.get("save_raw_phase") is not None) else None,
        saved_area_labels_output=execution.output_file(pathlib.Path(params.get("save_labels")).name + ".nii.gz") if (params.get("save_labels") is not None) else None,
    )
    return ret


def prelude_execute(
    params: PreludeParameters,
    execution: Execution,
) -> PreludeOutputs:
    """
    Phase Region Expanding Labeller for Unwrapping Discrete Estimates.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PreludeOutputs`).
    """
    params = execution.params(params)
    cargs = prelude_cargs(params, execution)
    ret = prelude_outputs(params, execution)
    execution.run(cargs)
    return ret


def prelude(
    output_unwrap: str,
    output_unwrap_alias: InputPathType,
    complex_phase: InputPathType | None = None,
    complex_phase_alias: InputPathType | None = None,
    absolute_volume: InputPathType | None = None,
    absolute_volume_alias: InputPathType | None = None,
    phase_volume: InputPathType | None = None,
    phase_volume_alias: InputPathType | None = None,
    num_phase_split: float | None = None,
    label_slices: bool = False,
    slice_processing: bool = False,
    slice_processing_alias: bool = False,
    force_3d: bool = False,
    force_3d_alias: bool = False,
    threshold: float | None = None,
    threshold_alias: float | None = None,
    mask_volume: InputPathType | None = None,
    mask_volume_alias: InputPathType | None = None,
    start_image: float | None = None,
    end_image: float | None = None,
    save_mask: InputPathType | None = None,
    save_raw_phase: InputPathType | None = None,
    save_raw_phase_alias: InputPathType | None = None,
    save_labels: InputPathType | None = None,
    save_labels_alias: InputPathType | None = None,
    remove_ramps: bool = False,
    verbose: bool = False,
    verbose_alias: bool = False,
    help_: bool = False,
    help_alias: bool = False,
    runner: Runner | None = None,
) -> PreludeOutputs:
    """
    Phase Region Expanding Labeller for Unwrapping Discrete Estimates.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output_unwrap: Filename for saving the unwrapped phase output.
        output_unwrap_alias: Filename for saving the unwrapped phase output.
        complex_phase: Filename of complex phase input volume.
        complex_phase_alias: Filename of complex phase input volume.
        absolute_volume: Filename of absolute input volume.
        absolute_volume_alias: Filename of absolute input volume.
        phase_volume: Filename of raw phase input volume.
        phase_volume_alias: Filename of raw phase input volume.
        num_phase_split: Number of phase partitions to use.
        label_slices: Does label processing in 2D (slice at a time).
        slice_processing: Does all processing in 2D (slice at a time).
        slice_processing_alias: Does all processing in 2D (slice at a time).
        force_3d: Forces all processing to be full 3D.
        force_3d_alias: Forces all processing to be full 3D.
        threshold: Intensity threshold for masking.
        threshold_alias: Intensity threshold for masking.
        mask_volume: Filename of mask input volume.
        mask_volume_alias: Filename of mask input volume.
        start_image: First image number to process (default 0).
        end_image: Final image number to process (default Inf).
        save_mask: Filename for saving the mask volume.
        save_raw_phase: Filename for saving the raw phase output.
        save_raw_phase_alias: Filename for saving the raw phase output.
        save_labels: Filename for saving the area labels output.
        save_labels_alias: Filename for saving the area labels output.
        remove_ramps: Remove phase ramps during unwrapping.
        verbose: Switch on diagnostic messages.
        verbose_alias: Switch on diagnostic messages.
        help_: Display help message.
        help_alias: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PreludeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PRELUDE_METADATA)
    params = prelude_params(
        output_unwrap=output_unwrap,
        output_unwrap_alias=output_unwrap_alias,
        complex_phase=complex_phase,
        complex_phase_alias=complex_phase_alias,
        absolute_volume=absolute_volume,
        absolute_volume_alias=absolute_volume_alias,
        phase_volume=phase_volume,
        phase_volume_alias=phase_volume_alias,
        num_phase_split=num_phase_split,
        label_slices=label_slices,
        slice_processing=slice_processing,
        slice_processing_alias=slice_processing_alias,
        force_3d=force_3d,
        force_3d_alias=force_3d_alias,
        threshold=threshold,
        threshold_alias=threshold_alias,
        mask_volume=mask_volume,
        mask_volume_alias=mask_volume_alias,
        start_image=start_image,
        end_image=end_image,
        save_mask=save_mask,
        save_raw_phase=save_raw_phase,
        save_raw_phase_alias=save_raw_phase_alias,
        save_labels=save_labels,
        save_labels_alias=save_labels_alias,
        remove_ramps=remove_ramps,
        verbose=verbose,
        verbose_alias=verbose_alias,
        help_=help_,
        help_alias=help_alias,
    )
    return prelude_execute(params, execution)


__all__ = [
    "PRELUDE_METADATA",
    "PreludeOutputs",
    "PreludeParameters",
    "prelude",
    "prelude_params",
]
