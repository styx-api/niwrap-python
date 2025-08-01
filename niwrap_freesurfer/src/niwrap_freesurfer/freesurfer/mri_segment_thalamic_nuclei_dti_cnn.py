# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SEGMENT_THALAMIC_NUCLEI_DTI_CNN_METADATA = Metadata(
    id="d893715e795f9e42e07a8cb788e3c2e50b141260.boutiques",
    name="mri_segment_thalamic_nuclei_dti_cnn",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriSegmentThalamicNucleiDtiCnnParameters = typing.TypedDict('MriSegmentThalamicNucleiDtiCnnParameters', {
    "__STYXTYPE__": typing.Literal["mri_segment_thalamic_nuclei_dti_cnn"],
    "t1_images": InputPathType,
    "aseg": typing.NotRequired[InputPathType | None],
    "fa": InputPathType,
    "v1": InputPathType,
    "output": str,
    "volume_output": typing.NotRequired[str | None],
    "posteriors_output": typing.NotRequired[str | None],
    "threads": typing.NotRequired[float | None],
    "force_cpu": bool,
    "model": typing.NotRequired[InputPathType | None],
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
        "mri_segment_thalamic_nuclei_dti_cnn": mri_segment_thalamic_nuclei_dti_cnn_cargs,
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
        "mri_segment_thalamic_nuclei_dti_cnn": mri_segment_thalamic_nuclei_dti_cnn_outputs,
    }.get(t)


class MriSegmentThalamicNucleiDtiCnnOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_segment_thalamic_nuclei_dti_cnn(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output: OutputPathType
    """Path to the segmentation output."""
    volume_csv: OutputPathType | None
    """CSV file with volumes for all structures."""
    posteriors: OutputPathType | None
    """Path to the posteriors output."""


def mri_segment_thalamic_nuclei_dti_cnn_params(
    t1_images: InputPathType,
    fa: InputPathType,
    v1: InputPathType,
    output: str,
    aseg: InputPathType | None = None,
    volume_output: str | None = None,
    posteriors_output: str | None = None,
    threads: float | None = None,
    force_cpu: bool = False,
    model: InputPathType | None = None,
) -> MriSegmentThalamicNucleiDtiCnnParameters:
    """
    Build parameters.
    
    Args:
        t1_images: Path to the T1 image(s) or folder containing images. These\
            must be registered to the FAs in physical coordinates.
        fa: Path to the FA image(s) or folder.
        v1: Path to the V1 image(s) or folder.
        output: Path to the segmentation output(s) or folder.
        aseg: Path to the ASEG segmentation(s) or folder. These must be\
            registered to the FAs in physical coordinates.
        volume_output: CSV file for volumes of all structures and subjects.
        posteriors_output: Path to the posteriors output(s) or folder.
        threads: Number of cores to be used. Default is 1.
        force_cpu: Enforce running with CPU rather than GPU.
        model: Path to an alternative model file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_segment_thalamic_nuclei_dti_cnn",
        "t1_images": t1_images,
        "fa": fa,
        "v1": v1,
        "output": output,
        "force_cpu": force_cpu,
    }
    if aseg is not None:
        params["aseg"] = aseg
    if volume_output is not None:
        params["volume_output"] = volume_output
    if posteriors_output is not None:
        params["posteriors_output"] = posteriors_output
    if threads is not None:
        params["threads"] = threads
    if model is not None:
        params["model"] = model
    return params


def mri_segment_thalamic_nuclei_dti_cnn_cargs(
    params: MriSegmentThalamicNucleiDtiCnnParameters,
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
    cargs.append("mri_segment_thalamic_nuclei_dti_cnn")
    cargs.extend([
        "--t1",
        execution.input_file(params.get("t1_images"))
    ])
    if params.get("aseg") is not None:
        cargs.extend([
            "--aseg",
            execution.input_file(params.get("aseg"))
        ])
    cargs.extend([
        "--fa",
        execution.input_file(params.get("fa"))
    ])
    cargs.extend([
        "--v1",
        execution.input_file(params.get("v1"))
    ])
    cargs.extend([
        "--o",
        params.get("output")
    ])
    if params.get("volume_output") is not None:
        cargs.extend([
            "--vol",
            params.get("volume_output")
        ])
    if params.get("posteriors_output") is not None:
        cargs.extend([
            "--post",
            params.get("posteriors_output")
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("force_cpu"):
        cargs.append("--cpu")
    if params.get("model") is not None:
        cargs.extend([
            "--model",
            execution.input_file(params.get("model"))
        ])
    return cargs


def mri_segment_thalamic_nuclei_dti_cnn_outputs(
    params: MriSegmentThalamicNucleiDtiCnnParameters,
    execution: Execution,
) -> MriSegmentThalamicNucleiDtiCnnOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSegmentThalamicNucleiDtiCnnOutputs(
        root=execution.output_file("."),
        segmentation_output=execution.output_file(params.get("output")),
        volume_csv=execution.output_file(params.get("volume_output")) if (params.get("volume_output") is not None) else None,
        posteriors=execution.output_file(params.get("posteriors_output")) if (params.get("posteriors_output") is not None) else None,
    )
    return ret


def mri_segment_thalamic_nuclei_dti_cnn_execute(
    params: MriSegmentThalamicNucleiDtiCnnParameters,
    execution: Execution,
) -> MriSegmentThalamicNucleiDtiCnnOutputs:
    """
    Thalamic segmentation tool providing 0.7mm isotropic thalamus segmentation from
    registered T1, FA, and V1 volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSegmentThalamicNucleiDtiCnnOutputs`).
    """
    params = execution.params(params)
    cargs = mri_segment_thalamic_nuclei_dti_cnn_cargs(params, execution)
    ret = mri_segment_thalamic_nuclei_dti_cnn_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_segment_thalamic_nuclei_dti_cnn(
    t1_images: InputPathType,
    fa: InputPathType,
    v1: InputPathType,
    output: str,
    aseg: InputPathType | None = None,
    volume_output: str | None = None,
    posteriors_output: str | None = None,
    threads: float | None = None,
    force_cpu: bool = False,
    model: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriSegmentThalamicNucleiDtiCnnOutputs:
    """
    Thalamic segmentation tool providing 0.7mm isotropic thalamus segmentation from
    registered T1, FA, and V1 volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1_images: Path to the T1 image(s) or folder containing images. These\
            must be registered to the FAs in physical coordinates.
        fa: Path to the FA image(s) or folder.
        v1: Path to the V1 image(s) or folder.
        output: Path to the segmentation output(s) or folder.
        aseg: Path to the ASEG segmentation(s) or folder. These must be\
            registered to the FAs in physical coordinates.
        volume_output: CSV file for volumes of all structures and subjects.
        posteriors_output: Path to the posteriors output(s) or folder.
        threads: Number of cores to be used. Default is 1.
        force_cpu: Enforce running with CPU rather than GPU.
        model: Path to an alternative model file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSegmentThalamicNucleiDtiCnnOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SEGMENT_THALAMIC_NUCLEI_DTI_CNN_METADATA)
    params = mri_segment_thalamic_nuclei_dti_cnn_params(
        t1_images=t1_images,
        aseg=aseg,
        fa=fa,
        v1=v1,
        output=output,
        volume_output=volume_output,
        posteriors_output=posteriors_output,
        threads=threads,
        force_cpu=force_cpu,
        model=model,
    )
    return mri_segment_thalamic_nuclei_dti_cnn_execute(params, execution)


__all__ = [
    "MRI_SEGMENT_THALAMIC_NUCLEI_DTI_CNN_METADATA",
    "MriSegmentThalamicNucleiDtiCnnOutputs",
    "MriSegmentThalamicNucleiDtiCnnParameters",
    "mri_segment_thalamic_nuclei_dti_cnn",
    "mri_segment_thalamic_nuclei_dti_cnn_params",
]
