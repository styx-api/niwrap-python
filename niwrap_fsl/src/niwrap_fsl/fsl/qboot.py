# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

QBOOT_METADATA = Metadata(
    id="44b4ad667be58d27640766d256a8ce58b6c36402.boutiques",
    name="qboot",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


QbootParameters = typing.TypedDict('QbootParameters', {
    "__STYX_TYPE__": typing.Literal["qboot"],
    "data_file": InputPathType,
    "mask_file": InputPathType,
    "bvecs_file": InputPathType,
    "bvals_file": InputPathType,
    "log_dir": typing.NotRequired[str | None],
    "forcedir_flag": bool,
    "q_file": typing.NotRequired[InputPathType | None],
    "model_type": typing.NotRequired[int | None],
    "lmax_order": typing.NotRequired[int | None],
    "npeaks": typing.NotRequired[int | None],
    "threshold": typing.NotRequired[float | None],
    "num_samples": typing.NotRequired[int | None],
    "lambda_param": typing.NotRequired[float | None],
    "delta_param": typing.NotRequired[float | None],
    "alpha_param": typing.NotRequired[float | None],
    "seed_param": typing.NotRequired[int | None],
    "gfa_flag": bool,
    "savecoeff_flag": bool,
    "savemeancoeff_flag": bool,
    "verbose_flag": bool,
    "help_flag": bool,
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
        "qboot": qboot_cargs,
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
        "qboot": qboot_outputs,
    }.get(t)


class QbootOutputs(typing.NamedTuple):
    """
    Output object returned when calling `qboot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Output files saved in the specified log directory"""


def qboot_params(
    data_file: InputPathType,
    mask_file: InputPathType,
    bvecs_file: InputPathType,
    bvals_file: InputPathType,
    log_dir: str | None = None,
    forcedir_flag: bool = False,
    q_file: InputPathType | None = None,
    model_type: int | None = None,
    lmax_order: int | None = None,
    npeaks: int | None = None,
    threshold: float | None = None,
    num_samples: int | None = None,
    lambda_param: float | None = None,
    delta_param: float | None = None,
    alpha_param: float | None = None,
    seed_param: int | None = None,
    gfa_flag: bool = False,
    savecoeff_flag: bool = False,
    savemeancoeff_flag: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
) -> QbootParameters:
    """
    Build parameters.
    
    Args:
        data_file: Data file.
        mask_file: Mask file.
        bvecs_file: b vectors file.
        bvals_file: b values file.
        log_dir: Output directory (default is logdir).
        forcedir_flag: Use the actual directory name given - i.e. don't add +\
            to make a new directory.
        q_file: File provided with multi-shell data. Indicates the number of\
            directions for each shell.
        model_type: Which model to use. 1=Tuch's ODFs, 2=CSA ODFs (default),\
            3=multi-shell CSA ODFs.
        lmax_order: Maximum spherical harmonic order employed (must be even,\
            default=4).
        npeaks: Maximum number of ODF peaks to be detected (default 2).
        threshold: Minimum threshold for a local maxima to be considered an ODF\
            peak. Expressed as a fraction of the maximum ODF value (default 0.4).
        num_samples: Number of bootstrap samples (default is 50).
        lambda_param: Laplace-Beltrami regularization parameter (default is 0).
        delta_param: Signal attenuation regularization parameter for models=2,3\
            (default is 0.01).
        alpha_param: Laplacian sharpening parameter for model=1 (default is 0,\
            should be smaller than 1).
        seed_param: Seed for pseudo-random number generator.
        gfa_flag: Compute a generalised FA, using the mean ODF in each voxel.
        savecoeff_flag: Save the ODF coefficients instead of the peaks.\
            WARNING: These can be huge files, please use a few bootstrap samples\
            and a low lmax!.
        savemeancoeff_flag: Save the mean ODF coefficients across all samples.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display this help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "qboot",
        "data_file": data_file,
        "mask_file": mask_file,
        "bvecs_file": bvecs_file,
        "bvals_file": bvals_file,
        "forcedir_flag": forcedir_flag,
        "gfa_flag": gfa_flag,
        "savecoeff_flag": savecoeff_flag,
        "savemeancoeff_flag": savemeancoeff_flag,
        "verbose_flag": verbose_flag,
        "help_flag": help_flag,
    }
    if log_dir is not None:
        params["log_dir"] = log_dir
    if q_file is not None:
        params["q_file"] = q_file
    if model_type is not None:
        params["model_type"] = model_type
    if lmax_order is not None:
        params["lmax_order"] = lmax_order
    if npeaks is not None:
        params["npeaks"] = npeaks
    if threshold is not None:
        params["threshold"] = threshold
    if num_samples is not None:
        params["num_samples"] = num_samples
    if lambda_param is not None:
        params["lambda_param"] = lambda_param
    if delta_param is not None:
        params["delta_param"] = delta_param
    if alpha_param is not None:
        params["alpha_param"] = alpha_param
    if seed_param is not None:
        params["seed_param"] = seed_param
    return params


def qboot_cargs(
    params: QbootParameters,
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
    cargs.append("qboot")
    cargs.extend([
        "-k",
        execution.input_file(params.get("data_file"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("mask_file"))
    ])
    cargs.extend([
        "-r",
        execution.input_file(params.get("bvecs_file"))
    ])
    cargs.extend([
        "-b",
        execution.input_file(params.get("bvals_file"))
    ])
    if params.get("log_dir") is not None:
        cargs.extend([
            "--ld",
            params.get("log_dir")
        ])
    if params.get("forcedir_flag"):
        cargs.append("--forcedir")
    if params.get("q_file") is not None:
        cargs.extend([
            "--q",
            execution.input_file(params.get("q_file"))
        ])
    if params.get("model_type") is not None:
        cargs.extend([
            "--model",
            str(params.get("model_type"))
        ])
    if params.get("lmax_order") is not None:
        cargs.extend([
            "--lmax",
            str(params.get("lmax_order"))
        ])
    if params.get("npeaks") is not None:
        cargs.extend([
            "--npeaks",
            str(params.get("npeaks"))
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "--thr",
            str(params.get("threshold"))
        ])
    if params.get("num_samples") is not None:
        cargs.extend([
            "--ns",
            str(params.get("num_samples"))
        ])
    if params.get("lambda_param") is not None:
        cargs.extend([
            "--lambda",
            str(params.get("lambda_param"))
        ])
    if params.get("delta_param") is not None:
        cargs.extend([
            "--delta",
            str(params.get("delta_param"))
        ])
    if params.get("alpha_param") is not None:
        cargs.extend([
            "--alpha",
            str(params.get("alpha_param"))
        ])
    if params.get("seed_param") is not None:
        cargs.extend([
            "--seed",
            str(params.get("seed_param"))
        ])
    if params.get("gfa_flag"):
        cargs.append("--gfa")
    if params.get("savecoeff_flag"):
        cargs.append("--savecoeff")
    if params.get("savemeancoeff_flag"):
        cargs.append("--savemeancoeff")
    if params.get("verbose_flag"):
        cargs.append("-V")
    if params.get("help_flag"):
        cargs.append("-h")
    return cargs


def qboot_outputs(
    params: QbootParameters,
    execution: Execution,
) -> QbootOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = QbootOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file("logdir/*"),
    )
    return ret


def qboot_execute(
    params: QbootParameters,
    execution: Execution,
) -> QbootOutputs:
    """
    Tool for computing q-ball ODFs using bootstrap samples.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `QbootOutputs`).
    """
    params = execution.params(params)
    cargs = qboot_cargs(params, execution)
    ret = qboot_outputs(params, execution)
    execution.run(cargs)
    return ret


def qboot(
    data_file: InputPathType,
    mask_file: InputPathType,
    bvecs_file: InputPathType,
    bvals_file: InputPathType,
    log_dir: str | None = None,
    forcedir_flag: bool = False,
    q_file: InputPathType | None = None,
    model_type: int | None = None,
    lmax_order: int | None = None,
    npeaks: int | None = None,
    threshold: float | None = None,
    num_samples: int | None = None,
    lambda_param: float | None = None,
    delta_param: float | None = None,
    alpha_param: float | None = None,
    seed_param: int | None = None,
    gfa_flag: bool = False,
    savecoeff_flag: bool = False,
    savemeancoeff_flag: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> QbootOutputs:
    """
    Tool for computing q-ball ODFs using bootstrap samples.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        data_file: Data file.
        mask_file: Mask file.
        bvecs_file: b vectors file.
        bvals_file: b values file.
        log_dir: Output directory (default is logdir).
        forcedir_flag: Use the actual directory name given - i.e. don't add +\
            to make a new directory.
        q_file: File provided with multi-shell data. Indicates the number of\
            directions for each shell.
        model_type: Which model to use. 1=Tuch's ODFs, 2=CSA ODFs (default),\
            3=multi-shell CSA ODFs.
        lmax_order: Maximum spherical harmonic order employed (must be even,\
            default=4).
        npeaks: Maximum number of ODF peaks to be detected (default 2).
        threshold: Minimum threshold for a local maxima to be considered an ODF\
            peak. Expressed as a fraction of the maximum ODF value (default 0.4).
        num_samples: Number of bootstrap samples (default is 50).
        lambda_param: Laplace-Beltrami regularization parameter (default is 0).
        delta_param: Signal attenuation regularization parameter for models=2,3\
            (default is 0.01).
        alpha_param: Laplacian sharpening parameter for model=1 (default is 0,\
            should be smaller than 1).
        seed_param: Seed for pseudo-random number generator.
        gfa_flag: Compute a generalised FA, using the mean ODF in each voxel.
        savecoeff_flag: Save the ODF coefficients instead of the peaks.\
            WARNING: These can be huge files, please use a few bootstrap samples\
            and a low lmax!.
        savemeancoeff_flag: Save the mean ODF coefficients across all samples.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display this help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QbootOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QBOOT_METADATA)
    params = qboot_params(
        data_file=data_file,
        mask_file=mask_file,
        bvecs_file=bvecs_file,
        bvals_file=bvals_file,
        log_dir=log_dir,
        forcedir_flag=forcedir_flag,
        q_file=q_file,
        model_type=model_type,
        lmax_order=lmax_order,
        npeaks=npeaks,
        threshold=threshold,
        num_samples=num_samples,
        lambda_param=lambda_param,
        delta_param=delta_param,
        alpha_param=alpha_param,
        seed_param=seed_param,
        gfa_flag=gfa_flag,
        savecoeff_flag=savecoeff_flag,
        savemeancoeff_flag=savemeancoeff_flag,
        verbose_flag=verbose_flag,
        help_flag=help_flag,
    )
    return qboot_execute(params, execution)


__all__ = [
    "QBOOT_METADATA",
    "QbootOutputs",
    "QbootParameters",
    "qboot",
    "qboot_params",
]
