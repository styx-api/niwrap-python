# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RUN_SAMSEG_LONG_METADATA = Metadata(
    id="281cafde4435543fa9734d7698891e798550c9ed.boutiques",
    name="run_samseg_long",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


RunSamsegLongParameters = typing.TypedDict('RunSamsegLongParameters', {
    "__STYX_TYPE__": typing.Literal["run_samseg_long"],
    "timepoint": list[InputPathType],
    "output": str,
    "lesion": bool,
    "threshold": typing.NotRequired[float | None],
    "samples": typing.NotRequired[float | None],
    "burnin": typing.NotRequired[float | None],
    "lesion_mask_structure": typing.NotRequired[str | None],
    "lesion_mask_pattern": typing.NotRequired[list[float] | None],
    "mode": typing.NotRequired[list[str] | None],
    "atlas": typing.NotRequired[str | None],
    "deformation_hyperprior": typing.NotRequired[float | None],
    "gmm_hyperprior": typing.NotRequired[float | None],
    "save_warp": bool,
    "save_mesh": bool,
    "save_posteriors": typing.NotRequired[list[str] | None],
    "pallidum_separate": bool,
    "threads": typing.NotRequired[float | None],
    "tp_to_base_transform": typing.NotRequired[list[InputPathType] | None],
    "force_different_resolutions": bool,
    "history": bool,
    "showfigs": bool,
    "movie": bool,
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
        "run_samseg_long": run_samseg_long_cargs,
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


class RunSamsegLongOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_samseg_long(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def run_samseg_long_params(
    timepoint: list[InputPathType],
    output: str,
    lesion: bool = False,
    threshold: float | None = None,
    samples: float | None = None,
    burnin: float | None = None,
    lesion_mask_structure: str | None = None,
    lesion_mask_pattern: list[float] | None = None,
    mode: list[str] | None = None,
    atlas: str | None = None,
    deformation_hyperprior: float | None = None,
    gmm_hyperprior: float | None = None,
    save_warp: bool = False,
    save_mesh: bool = False,
    save_posteriors: list[str] | None = None,
    pallidum_separate: bool = False,
    threads: float | None = None,
    tp_to_base_transform: list[InputPathType] | None = None,
    force_different_resolutions: bool = False,
    history: bool = False,
    showfigs: bool = False,
    movie: bool = False,
) -> RunSamsegLongParameters:
    """
    Build parameters.
    
    Args:
        timepoint: Configure a timepoint with multiple inputs.
        output: Output directory.
        lesion: Enable lesion segmentation (requires tensorflow).
        threshold: Lesion threshold for final segmentation. Requires lesion\
            segmentation.
        samples: Number of samples for lesion segmentation. Requires lesion\
            segmentation.
        burnin: Number of burn-in samples for lesion segmentation. Requires\
            lesion segmentation.
        lesion_mask_structure: Intensity mask brain structure. Requires lesion\
            segmentation.
        lesion_mask_pattern: Lesion mask list: -1 below lesion mask structure\
            mean, +1 above, 0 no mask. Requires lesion segmentation.
        mode: Output basenames for the input image mode.
        atlas: Point to an alternative atlas directory.
        deformation_hyperprior: Strength of the latent deformation hyperprior.
        gmm_hyperprior: Strength of the latent GMM hyperprior.
        save_warp: Save the image->template warp fields.
        save_mesh: Save the final mesh of each timepoint in template space.
        save_posteriors: Save posterior volumes to the 'posteriors'\
            subdirectory.
        pallidum_separate: Move pallidum outside of global white matter class.\
            Use with T2/flair.
        threads: Number of threads to use. Defaults to OMP_NUM_THREADS or 1.
        tp_to_base_transform: Transformation file for each time point to base.
        force_different_resolutions: Force run even if time points have\
            different resolutions.
        history: Save history.
        showfigs: Show figures during run.
        movie: Show history as arrow key controlled time sequence.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "run_samseg_long",
        "timepoint": timepoint,
        "output": output,
        "lesion": lesion,
        "save_warp": save_warp,
        "save_mesh": save_mesh,
        "pallidum_separate": pallidum_separate,
        "force_different_resolutions": force_different_resolutions,
        "history": history,
        "showfigs": showfigs,
        "movie": movie,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if samples is not None:
        params["samples"] = samples
    if burnin is not None:
        params["burnin"] = burnin
    if lesion_mask_structure is not None:
        params["lesion_mask_structure"] = lesion_mask_structure
    if lesion_mask_pattern is not None:
        params["lesion_mask_pattern"] = lesion_mask_pattern
    if mode is not None:
        params["mode"] = mode
    if atlas is not None:
        params["atlas"] = atlas
    if deformation_hyperprior is not None:
        params["deformation_hyperprior"] = deformation_hyperprior
    if gmm_hyperprior is not None:
        params["gmm_hyperprior"] = gmm_hyperprior
    if save_posteriors is not None:
        params["save_posteriors"] = save_posteriors
    if threads is not None:
        params["threads"] = threads
    if tp_to_base_transform is not None:
        params["tp_to_base_transform"] = tp_to_base_transform
    return params


def run_samseg_long_cargs(
    params: RunSamsegLongParameters,
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
    cargs.append("run_samseg_long")
    cargs.extend([
        "-t",
        *[execution.input_file(f) for f in params.get("timepoint")]
    ])
    cargs.extend([
        "-o",
        params.get("output")
    ])
    if params.get("lesion"):
        cargs.append("--lesion")
    if params.get("threshold") is not None:
        cargs.extend([
            "--threshold",
            str(params.get("threshold"))
        ])
    if params.get("samples") is not None:
        cargs.extend([
            "--samples",
            str(params.get("samples"))
        ])
    if params.get("burnin") is not None:
        cargs.extend([
            "--burnin",
            str(params.get("burnin"))
        ])
    if params.get("lesion_mask_structure") is not None:
        cargs.extend([
            "--lesion-mask-structure",
            params.get("lesion_mask_structure")
        ])
    if params.get("lesion_mask_pattern") is not None:
        cargs.extend([
            "--lesion-mask-pattern",
            *map(str, params.get("lesion_mask_pattern"))
        ])
    if params.get("mode") is not None:
        cargs.extend([
            "-m",
            *params.get("mode")
        ])
    if params.get("atlas") is not None:
        cargs.extend([
            "-a",
            params.get("atlas")
        ])
    if params.get("deformation_hyperprior") is not None:
        cargs.extend([
            "--deformation-hyperprior",
            str(params.get("deformation_hyperprior"))
        ])
    if params.get("gmm_hyperprior") is not None:
        cargs.extend([
            "--gmm-hyperprior",
            str(params.get("gmm_hyperprior"))
        ])
    if params.get("save_warp"):
        cargs.append("--save-warp")
    if params.get("save_mesh"):
        cargs.append("--save-mesh")
    if params.get("save_posteriors") is not None:
        cargs.extend([
            "--save-posteriors",
            *params.get("save_posteriors")
        ])
    if params.get("pallidum_separate"):
        cargs.append("--pallidum-separate")
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("tp_to_base_transform") is not None:
        cargs.extend([
            "--tp-to-base-transform",
            *[execution.input_file(f) for f in params.get("tp_to_base_transform")]
        ])
    if params.get("force_different_resolutions"):
        cargs.append("--force-different-resolutions")
    if params.get("history"):
        cargs.append("--history")
    if params.get("showfigs"):
        cargs.append("--showfigs")
    if params.get("movie"):
        cargs.append("--movie")
    return cargs


def run_samseg_long_outputs(
    params: RunSamsegLongParameters,
    execution: Execution,
) -> RunSamsegLongOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RunSamsegLongOutputs(
        root=execution.output_file("."),
    )
    return ret


def run_samseg_long_execute(
    params: RunSamsegLongParameters,
    execution: Execution,
) -> RunSamsegLongOutputs:
    """
    Longitudinal image segmentation using SAMSEG.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RunSamsegLongOutputs`).
    """
    params = execution.params(params)
    cargs = run_samseg_long_cargs(params, execution)
    ret = run_samseg_long_outputs(params, execution)
    execution.run(cargs)
    return ret


def run_samseg_long(
    timepoint: list[InputPathType],
    output: str,
    lesion: bool = False,
    threshold: float | None = None,
    samples: float | None = None,
    burnin: float | None = None,
    lesion_mask_structure: str | None = None,
    lesion_mask_pattern: list[float] | None = None,
    mode: list[str] | None = None,
    atlas: str | None = None,
    deformation_hyperprior: float | None = None,
    gmm_hyperprior: float | None = None,
    save_warp: bool = False,
    save_mesh: bool = False,
    save_posteriors: list[str] | None = None,
    pallidum_separate: bool = False,
    threads: float | None = None,
    tp_to_base_transform: list[InputPathType] | None = None,
    force_different_resolutions: bool = False,
    history: bool = False,
    showfigs: bool = False,
    movie: bool = False,
    runner: Runner | None = None,
) -> RunSamsegLongOutputs:
    """
    Longitudinal image segmentation using SAMSEG.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        timepoint: Configure a timepoint with multiple inputs.
        output: Output directory.
        lesion: Enable lesion segmentation (requires tensorflow).
        threshold: Lesion threshold for final segmentation. Requires lesion\
            segmentation.
        samples: Number of samples for lesion segmentation. Requires lesion\
            segmentation.
        burnin: Number of burn-in samples for lesion segmentation. Requires\
            lesion segmentation.
        lesion_mask_structure: Intensity mask brain structure. Requires lesion\
            segmentation.
        lesion_mask_pattern: Lesion mask list: -1 below lesion mask structure\
            mean, +1 above, 0 no mask. Requires lesion segmentation.
        mode: Output basenames for the input image mode.
        atlas: Point to an alternative atlas directory.
        deformation_hyperprior: Strength of the latent deformation hyperprior.
        gmm_hyperprior: Strength of the latent GMM hyperprior.
        save_warp: Save the image->template warp fields.
        save_mesh: Save the final mesh of each timepoint in template space.
        save_posteriors: Save posterior volumes to the 'posteriors'\
            subdirectory.
        pallidum_separate: Move pallidum outside of global white matter class.\
            Use with T2/flair.
        threads: Number of threads to use. Defaults to OMP_NUM_THREADS or 1.
        tp_to_base_transform: Transformation file for each time point to base.
        force_different_resolutions: Force run even if time points have\
            different resolutions.
        history: Save history.
        showfigs: Show figures during run.
        movie: Show history as arrow key controlled time sequence.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunSamsegLongOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_SAMSEG_LONG_METADATA)
    params = run_samseg_long_params(
        timepoint=timepoint,
        output=output,
        lesion=lesion,
        threshold=threshold,
        samples=samples,
        burnin=burnin,
        lesion_mask_structure=lesion_mask_structure,
        lesion_mask_pattern=lesion_mask_pattern,
        mode=mode,
        atlas=atlas,
        deformation_hyperprior=deformation_hyperprior,
        gmm_hyperprior=gmm_hyperprior,
        save_warp=save_warp,
        save_mesh=save_mesh,
        save_posteriors=save_posteriors,
        pallidum_separate=pallidum_separate,
        threads=threads,
        tp_to_base_transform=tp_to_base_transform,
        force_different_resolutions=force_different_resolutions,
        history=history,
        showfigs=showfigs,
        movie=movie,
    )
    return run_samseg_long_execute(params, execution)


__all__ = [
    "RUN_SAMSEG_LONG_METADATA",
    "RunSamsegLongOutputs",
    "RunSamsegLongParameters",
    "run_samseg_long",
    "run_samseg_long_params",
]
